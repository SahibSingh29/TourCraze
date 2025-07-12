from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CusUser
from .models import ToursDetails
from .models import HotelDetails
from .models import RestaurantDetais
from django import forms
from .models import Post, Comment

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CusUser
        fields = ["name", "username",  "email", "password1", "password2"]

class UpdateUser(ModelForm): 
    class Meta:
        model = CusUser
        fields  = ["name", "avatar", "username",  "email", "bio"]

class ToursDetailsForm(forms.ModelForm):
    class Meta:
        model = ToursDetails
        fields = ['tour_name', 'phone_number', 'rate', 'detail', 'destination', 'email']
        widgets = {
            'tour_name': forms.TextInput(attrs={
                'class': 'custom-tour-name-input',
                'placeholder': 'Enter Tour Name'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'custom-phone-input',
                'placeholder': 'Enter Phone Number'
            }),
            'rate': forms.NumberInput(attrs={
                'class': 'custom-rate-input',
                'placeholder': 'Enter Rate'
            }),
            'detail': forms.Textarea(attrs={
                'class': 'custom-detail-input',
                'placeholder': 'Enter Details about the Tour',
                'rows': 4,
            }),
            'destination': forms.TextInput(attrs={
                'class': 'custom-destination-input',
                'placeholder': 'Enter Destination'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'custom-email-input',
                'placeholder': 'Enter Email Address'
            }),
        }

class HotelDetailsForm(forms.ModelForm):
    class Meta:
        model = HotelDetails
        fields = ['hotel_name', 'phone_number', 'email', 'location']
        widgets = {
            'hotel_name': forms.TextInput(attrs={
                'class': 'custom-hotel-name-input',
                'placeholder': 'Enter Hotel Name'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'custom-phone-input',
                'placeholder': 'Enter Phone Number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'custom-email-input',
                'placeholder': 'Enter Email Address'
            }),
            'location': forms.TextInput(attrs={
                'class': 'custom-location-input',
                'placeholder': 'Enter Location'
            }),
        }

class RestaurantDetailsForm(forms.ModelForm):
    class Meta:
        model = RestaurantDetais
        fields = ['restaurnt_name', 'location', 'phone_number', 'email']

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'custom-content-input',
                'placeholder': 'Enter your content here...',
                'rows': 4,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'custom-image-input',
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']