from django.db import models

# Create your models here.


class MyModel(models.Model):
    """Models for database"""
    link = models.CharField(max_length=1000)
    unique_id = models.CharField(max_length=5)

    def __str__(self):
        return self.link
