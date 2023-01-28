
from django.db import models

class Wine101(models.Model):

    wine101_id = models.CharField(max_length=100)
    content = models.CharField(max_length=50)
    article_image = models.CharField(max_length=100)
    article_link = models.CharField(max_length=150)
    profile_id = models.CharField(max_length=100)
