from django.db import models
# from wineadventureapi.models import Wine, Category
from .wine import Wine
from .category import Category

class Wine_Category(models.Model):

    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name = 'winecat')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
