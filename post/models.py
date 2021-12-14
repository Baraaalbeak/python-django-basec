from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey


class Post(models.Model):
    title=models.CharField(max_length=30)
    body=models.TextField()
    

# Create your models here.
