from django.test import TestCase
from django.test import SimpleTestCase
from django.contrib.auth.models import User
from .models import Video
from django.urls import reverse
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

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

class HomeTest(LiveServerTestCase):
    def test_chromehome(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')

        time.sleep(5)

        assert "The Debrary" in driver.title

class LoginTest(LiveServerTestCase):
    def testLogin(self):
        driver = webdriver.Chrome()

        driver.get("http://127.0.0.1:8000/accounts/login/")

        time.sleep(3)

        user_name = driver.find_element(By.NAME, 'username')
        user_password = driver.find_element(By.NAME, 'password')

        time.sleep(3)

        submit = driver.find_element(By.NAME, 'button1')


        user_name.send_keys('admin')
        user_password.send_keys('admin')

        submit.send_keys(Keys.RETURN)

        assert 'admin' in driver.page_source
