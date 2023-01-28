
from django.db import models
from .profile import Profile

class Wine101(models.Model):

    article_name = models.CharField(max_length=50)
    context = models.CharField(max_length=100)
    article_image = models.CharField(max_length=100)
    article_link = models.CharField(max_length=150)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
