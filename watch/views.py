from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood, UserProfile, Business, EmergencyContacts, Post
from .forms import NeighbourhoodForm, UpdateProfileForm, AddBusinessForm, PostForm
from django.urls import reverse

# Create your views here.
def index