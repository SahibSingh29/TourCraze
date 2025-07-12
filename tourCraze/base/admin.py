from django.contrib import admin
from .models import  CusUser, Location, ToursDetails, HotelDetails, RestaurantDetais, Post, Comment, Like

admin.site.register(CusUser)
admin.site.register(Location)
admin.site.register(ToursDetails)
admin.site.register(HotelDetails)
admin.site.register(RestaurantDetais)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
