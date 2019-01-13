from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Neighbourhood(models.Model):


    '''
    Neighbourhood class has the following properties
    '''

    neighborhood_name = models.CharField(max_length = 30)
    # neighborhood_location = models.ForeignKey('Location', on_delete = models.CASCADE)
    occupants = models.IntegerField(null = True)
    admin = models.ForeignKey(User, on_delete = models.CASCADE)

    def create_neighbourhood(self):
        self.save

    def delete_neighbourhood(self):
        seld.delete()

    def __str__(self):
        return self.name

    @classmethod
    def find_neighbourhood(cls, neighbourhood_id):
        neighbourhood = cls.objects.get(id = neighbourhood_id)
        return neighbourhood

    def update_nighbourhood(self):
        self.save()

    def update_occupants(self):
        self.occupants +=1
        self.save()

class UserProfile(models.Model):
    '''
    UserProfile class has the following properties
    '''

    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    email = models.EmailField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey('Neighbourhood', on_delete=models.CASCADE, null=True, blank=True)

    def assign_neighbourhood(self, neighbourhood):
        self.neighbourhood = neighborhood
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return f'{self.user.username}'

class Business(models.Model):
    business_name = models.CharField(max_length = 50)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    business_location = models.CharField(max_length=30, blank=True)
    business_neighbourhood = models.ForeignKey(
        'Neighbourhood', on_delete=models.CASCADE)
    email = models.EmailField()

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        business = cls.objects.get(id=business_id)
        return business

    def update_business(self, business_name):
        self.name = business_name
        self.save()

    def __str__(self):
        return f'{self.name}'


class EmergencyContacts(models.Model):
    name = models.CharField(max_length=30)
    contacts = models.CharField(max_length=20)
    email = models.EmailField()
    neighbourhood_contact = models.ForeignKey(
        'Neighbourhood', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name},{self.email}'
