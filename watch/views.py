from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import NeighbourhoodForm, UpdateProfileForm, AddBusinessForm, PostForm
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def location(request):
    if not request.user.is_authenticated:
       return redirect('signout')
    else:
        if request.user.id == 1:
            if request.method == 'POST':
                form = NeighbourhoodForm(request.POST)
                if form.is_valid():
                    neighbourhood = Neighbourhood(
                        neighbourhood_name=request.POST['neighbourhood_name'], neighbourhood_location=request.POST['neoghbourhood_location'])
                    neighbourhood.save()
                return redirect('location')
            else:
                form = NeighbourhoodForm()
                neighbourhoods = Neighbourhood.objects.all()
            return render(request, 'location.html', {'neighbourhoods': neighbourhoods, 'form': form})
        elif request.user != 1:
            user = UserProfile.objects.filter(user=request.user).first()
            if user is None:
                user = UserProfile(user=request.user)
                user.save()
                if user.neighborhood is None:
                    title = 'Neighbourhood'
                    neighbourhoods = Neighbourhood.objects.all()
                return render(request, 'location.html', {'neighbourhoods': neighbourhoods})
            else:
                user = UserProfile.objects.filter(user=request.user).first()
                return redirect(reverse('neighbourhood', args=[user.neighbourhood.id]))

def signout(request):
    logout(request)
    return redirect('login')

def neighbourhood(request, neighbourhood_id):
    if request.user.id == 1:
        neighbourhood = Neighbourhood.objects.get(id=neighbourhood_id)
        members = UserProfile.objects.filter(neighboruhood=neighbourhood).all()
        emergencies = EmergencyContacts.objects.filter(
            neighbourhood_contact=neighbourhood).all()
        return render(request, 'hood.html', {'neighbourhood': neighbourhood, 'members': members, 'emergencies': emergencies})
    else:
        neighbourhood = Neighbourhood.objects.get(id = neighbourhood_id)
        user = UserProfile.objects.filter(user = request.user).first()
        businesses = Business.objects.filter(business_neighbourhood=neighbourhood).all()
        emergencies = EmergencyContacts.objects.filter(neighbourhood_contact = neighbourhood).all()
        user.neighbourhood = neighbourhood
        user.save()

        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = Post(title=request.POST['title'],post_description=request.POST['post_description'],posted_by=request.user,post_hood=neighbourhood,posted_on=datetime.datetime.now())
                post.save()
                return redirect(reverse('neighbourhood',args=[neighbourhood.id]))
        else:
            form = PostForm()

        posts = Post.objects.filter(post_hood = neighborhood).all()
        return render(request,'hood.html',{'posts':posts,'form':form,'user':user,'businesses':businesses,'neighbourhood':neighbourhood,'emergencies':emergencies})

def change_neighbourhood(request, neighbourhood_id):
    profile = UserProfile.objects.filter(user=request.user).first()
    neighbourhood = Neighbourhood.objects.get(id=neighbourhood_id)
    profile.neighbourhood = neighbourhood
    profile.save()
    return redirect(reverse('neighbourhood',args=[neighbourhood.id]))

def profile(request, user_id):
    user = User.object.get(id=user_id)
    profile = UserProfile.objects.filter(user=user).first()
    if request.methid == 'POST':
        form = UpdateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile.first_name = request.POST['first_name']
            profile.last_name = request.POST['last_name']
            profile.location = request.POST['location']
            profile.save()
        return redirect(reverse('profile', args=[user.id]))
    else:
        form = UpdateProfileForm(instance=profile)

    businesses = Business.objects.filter(owner=user).all()
    emergencies = EmergencyContacts.objects.filter(
        neighborhood_contact = profile.neighborhood).all()
    neighborhoods=Neighborhood.objects.all()

    return render(request, 'profile.html', {'neighborhoods': neighborhoods, 'businesses': businesses, 'profile': profile, 'form': form, 'emergencies': emergencies})

def add_business(request):
    user=User.objects.filter(id = request.user.id).first()
    profile=UserProfile.objects.filter(user = user).first()
    if request.method == 'POST':
        business_form=AddBusinessForm(request.POST)
        if business_form.is_valid():
            business=Business(
                name = request.POST['name'], owner = user, business_neighbourhood = profile.neighbourhood, email = request.POST['email'])
            business.save()
        return redirect(reverse(profile, args=[user.id]))
    else:
        business_form=AddBusinessForm()
    return render(request, 'business.html', {'business_form': business_form})

def search(request):
    try:
        if 'business' in request.GET and request.GET['business']:
            search_term=request.GET.get('business')
            searched_business=Business.object.get(
                name__icontains = search_term)
            return render(request, 'search.html', {'searched_business': searched_business})
    except (ValueError, Business.DoNotExit):
        message='No such business found.'
        return render(request, 'search.html', {'message': message})
    return render(request, 'search.html', {'message': message, 'searched_business': searched_business})


def update_profile(request, id):
    if request.method == "POST":
        profile = Profile.objects.get(id=id)
        form = UpdateProfileForm(request.POST or None,request.FILES or None, instance=profile)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect('profile', username=request.user)
    else:
        form = UpdateProfileForm()
    return render(request, 'update_profile.html', {'form': form})
