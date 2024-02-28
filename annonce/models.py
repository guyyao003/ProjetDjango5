from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Ad(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="annonce", default="null")
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title
    
class Contact(models.Model):
    user = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    sujet = models.CharField(max_length=200)
    messages = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.user

# Create your models here.
