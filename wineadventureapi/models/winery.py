from django.db import models
from .category import Category
from .country import Country

class Winery(models.Model):
  
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    winery_name = models.CharField(max_length=50)
    details = models.CharField(max_length=50)
