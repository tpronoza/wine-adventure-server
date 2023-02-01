
from django.db import models
from .user import User

class Wine(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # winery_name =  models.CharField(max_length=100)
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
    @property
    def winecategory(self):
        winecategory = [categories for categories in self.winecat.all()]
        return winecategory
