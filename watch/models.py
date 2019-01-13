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
    email = models.CharField(max_length = 40, blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, null=True, blank=True)

    def assign_neighborhood(self, neighborhood):
        self.neighborhood = neighborhood
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return f'{self.user.username}'
