from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model


class Healthyfood(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    food_name=models.CharField(max_length=255)
    img_url=models.TextField(default='no img')
    description=models.TextField(blank=True)
    
    def __str__(self):
        return self.food_name


class Food_type(models.Model):
    
    food_name=models.CharField(max_length=255)
    
    description=models.TextField(blank=True)
    
    def __str__(self):
        return self.food_name