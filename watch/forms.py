from .models import Neighbourhood, Business, UserProfile, Post
from django.contrib.auth.models import User
from django import forms


class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('neighbourhood_name',)


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name')


class AddBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('business_name', 'email', 'business_neighbourhood')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_description',)
