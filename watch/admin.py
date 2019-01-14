from django.contrib import admin
from .models import Neighbourhood, UserProfile, Business, EmergencyContacts, Post

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(EmergencyContacts)
admin.site.register(Post)
