from django.test import TestCase
from django.test import SimpleTestCase
from django.contrib.auth.models import User
from .models import Video
from django.urls import reverse
from django.test import LiveServerTestCase
from selenium import webdriver

class PostModelTest(TestCase):
    def setUp(self):
        # Create a user and a post for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Video.videos.create(url='test url', description='This is a test post', platform="YT")

    def test_post_str(self):
        # Test that the _str_ method returns the title of the post
        self.assertEqual(str(self.post), 'test url')
# Create your tests here.
class HomepageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

class VideoListTest(TestCase):
    def test_url_available_by_name(self):  
        response = self.client.get(reverse("videos"))
        self.assertEqual(response.status_code, 200)

class LoginTest(LiveServerTestCase)
    def test_login(self):
        driver = webdriver.

class Test2