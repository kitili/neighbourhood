from django.test import TestCase
from .models import Profile, Neighbourhood
from django.contrib.auth.models import User
from watch.models import healthservices

# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    Test case for the Profile class and it's behaviours
    '''
    def setUp(self):
        '''
        Method that will run before any test case under this class
        '''
        self.new_user = User(username = "cate", email = "cateh@gmail.com", password = "dontbelittleyourself",)
        self.new_user.save()

        self.new_neigh = Neighbourhood(neighbourhood_name = "Imara")
        self.new_neigh.save()

        self.new_profile = Profile(username = self.new_user, neighbourhood = self.new_neigh, name = "bilal rock", email = "bilal@gmail.com", bio = "I see myself here")

    def test_instance(self):
        '''
        Test to confirm that the object is being instantiated correctly
        '''
        self.assertTrue(isinstance(self.new_profile, Profile))

    def tearDown(self):
        Profile.objects.all().delete()


class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Imara = Neighbourhood(neighbourhood_name = '')

    def test_instance(self):
        self.assertTrue(isinstance(self.Imara, Neighbourhood))

    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Imara.create_neighbourhood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_delete_method(self):
        self.Imara.delete_neighbourhood('Imara')
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) == 0)

    def test_find_neighbourhood(self):
        self.Imara.create_neighbourhood()
        fetched_hood = Neighbourhood.find_neighbourhood("Imara")
        self.assertNotEqual(fetched_hood, self.Imara)

    def test_update_method(self):
        self.Imara.create_neighbourhood()
        edited_hood = Neighbourhood.update_neighbourhood("mwiki")
        self.assertEqual(self.Imara, edited_hood)


class healthservicesTestClass(TestCase):
    def setUp(self):
        self.optical = healthservices(healthservices = 'optical')

    def test_instance(self):
        self.assertTrue(isinstance(self.optical, healthservices))

    def tearDown(self):
        healthservices.objects.all().delete()

    def test_save_method(self):
        self.optical.save_healthservices()
        health = healthservices.objects.all()
        self.assertTrue(len(health) > 0)

    def test_delete_method(self):
        self.optical.delete_healthservices('optical')
        health = healthservices.objects.all()
        self.assertTrue(len(health) == 0)