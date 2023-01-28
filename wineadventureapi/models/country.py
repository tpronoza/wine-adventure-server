from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=50)
