from django.test import TestCase
from django.contrib.auth.models import User
from .models import Neighbourhood, UserProfile, Business, EmergencyContacts, Post

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    '''
    Test class that define test cases for the neighbourhood class behaviour.

    Args:
        unittest.TestCase: TestCase class that helps in cresting test cases.
    '''
    # SetUp
    def SetUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_neighbourhood = Neoghbourhood(id=1, neighbourhood_name='Miotoni', neighbourhood_location='Karen', occupants=50)
    
    # instance
    def test_instance(self):
        '''
        test_instance test case to test if the object is instanciated properly
        '''
        def test_instance(self):
            self.assertTrue(isinstance(self.new_neighbourhood, Neighbourhood))
    
    # create
    def test_create_neighbourhood(self):
        '''
        test_create_neighbourhood test case to test if the neighbourhood object is created
        '''
        self.location.save()
        

    # delete
    # def test_delete_neighbourhood(self):
    #     '''
    #     test_delete_neighbourhood test case to test if the neighbourhood object is deleted
        

