from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=150,unique=True)
    def __str__(self):
        return self.name 
    


class News(models.Model):
    name=models.TextField()
    description=models.TextField()
    created_by=models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    views=models.IntegerField(default=0)
    pcimage=models.ImageField(upload_to="image",blank=True)
    urlimage=models.CharField(max_length=255, blank=True)
    category=models.ForeignKey(Category,related_name="category",on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

