
from django.db import models
from .user import User

class Wine101(models.Model):

    article_name = models.CharField(max_length=50)
    context = models.CharField(max_length=100)
    article_image = models.CharField(max_length=100)
    article_link = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
