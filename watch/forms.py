from .models import Neighbourhood, Business, UserProfile, Post
from django.contrib.auth.models import User
from django.forms import ModelForm


class NeighborrhoodForm(ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('neighborhood_name',)


class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'location')


class AddBusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'email', 'business_location')


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_description',)
