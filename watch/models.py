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

   
