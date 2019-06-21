from django.test import TestCase
import datetime as dt
from .models import Post

class PostTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.post= Post(title = 'First Post', content='This is my first posting', date_posted ='May 20, 2018', post_image='media/images/default.jpg')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def tearDown(self):
        Post.objects.all().delete()
    
   