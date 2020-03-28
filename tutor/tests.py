from django.test import TestCase, Client
from tutor.models import Subject, Profile, Job
from django.contrib.auth.models import User

# Create your tests here.

class DummyTestCase(TestCase):
    def setUp(self):
        x = 2

    def test_dummy_test_case(self):
        self.assertEqual(2, 2)

class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # creates dummy user object, can be reused in other tests
        test_user = User.objects.create_user(id=1, username='testuser', password='12345')
        Profile.objects.create(user=test_user, phone_number='4797998232', first_name='test', last_name='user', email_addr='test@gmail.com', rating=4.59)

    def test_first_name_max_length(self):
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 200)