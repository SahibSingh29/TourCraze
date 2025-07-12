from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# Create your models here.

class CusUser (AbstractUser):
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

class Location (models.Model):
    name = models.CharField(max_length=200, null=True)
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        null = True,
        default = 0,
    )
    
class EmgCon (models.Model):
    num =  models.TextField(null = True)

class ToursDetails(models.Model):
    tour_name = models.CharField(max_length=100, verbose_name="Tour Name")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    email = models.EmailField(max_length=100, verbose_name="Email Address")
    rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Rate")
    detail = models.CharField(max_length=200, verbose_name="Tour Detail")
    destination = models.CharField(max_length=200, verbose_name="Tour Destination")

def __str__(self):
        return self.name

class HotelDetails(models.Model):
    hotel_name = models.CharField(max_length=50, verbose_name="Hotel Name")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    email = models.EmailField(max_length=100, verbose_name="Email Address")
    location = models.CharField(max_length=200, verbose_name="Location")

def __str__(self):
        return self.name

class RestaurantDetais(models.Model):
    restaurnt_name = models.CharField(max_length=50, verbose_name="Restaurant Name")
    location = models.CharField(max_length=200, verbose_name="Location")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    email = models.EmailField(max_length=100, verbose_name="Email Address")

def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} - {self.content[:20]}'
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} - {self.content[:20]}'
    
class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='likes')

    def __str__(self):
        return f'{self.user.username} liked {self.post.id}'
