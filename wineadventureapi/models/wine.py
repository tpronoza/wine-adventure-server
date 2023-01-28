
from django.db import models
from .profile import Profile
from .winery import Winery

class Wine(models.Model):

    wine_name = models.CharField(max_length=100)
    year_produced = models.CharField(max_length=50)
    wine_picture = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    wine_type = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    favorite = models.BooleanField(default=False)
    wish_list = models.BooleanField(default=False)
    wine_list = models.BooleanField(default=False)
    uid = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    winery = models.ForeignKey(Winery, on_delete=models.CASCADE)
