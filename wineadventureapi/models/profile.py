from django.db import models
from .user import User

class Profile(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=1000)
    about_me = models.CharField(max_length=1000)
    favorite = models.CharField(max_length=1000)
    wish_list = models.CharField(max_length=1000)
    my_wines_list = models.CharField(max_length=1000)
    uid = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    