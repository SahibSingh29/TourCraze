from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import CusUser
from .forms import MyUserCreationForm, UpdateUser
from .models import ToursDetails
from .forms import ToursDetailsForm
from .forms import HotelDetailsForm
from .models import HotelDetails
from .forms import RestaurantDetailsForm
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm

import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home_page")
        else:
            messages.error(request, "Username or Password does not match!")

    return render(request, "base/login_page.html")

def maps(request):
    return render (request,"base/maps.html" )

def register_page(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        print(form.errors)
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home_page")
        else:
            messages.error(request, "An Error occured during registration!")
            print(form.errors)

    context = {"form": form}
    return render(request, "base/register_page.html", context)


@login_required(login_url="login_page")
def update_user(request, pk):
    user = request.user

    if request.user.username != pk:
        redirect(request, "base/home_page.html")

    form = UpdateUser(instance=user)

    if request.method == "POST":
        form = UpdateUser(request.POST, request.FILES, instance=user)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("update_user", pk=user.username)
        else:
            messages.error(request, "An Error occured during registration!")

    context = {pk: pk, form: form}
    return render(request, "base/update_user.html", context)


@login_required(login_url="login_page")
def home_page(request):
    context = {}
    return render(request, "base/home_page.html", context)

@login_required(login_url="login_page")
def tours(request, pk):
    context = {pk: pk}
    return render(request, "base/tours.html", context)

@login_required(login_url="login_page")
def tours_details(request):
    if request.method == 'POST':
        form = ToursDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form Data:", form.cleaned_data)
            tours_details=form.save()
            return redirect('tours_page', pk=tours_details.pk)
    else:
        form=ToursDetailsForm()
    return render(request, 'base/tours_registration.html',{'form':form})

@login_required(login_url="login_page")
def tours_page(request,pk):
    tours_details = ToursDetails.objects.all()

    return render(request, 'base/tours.html', {'tours_details': tours_details})

@login_required(login_url="login_page")
def hotel_details(request):
    if request.method == 'POST':
        form = HotelDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form Data:", form.cleaned_data)
            hotel_details=form.save()
            return redirect('hotel_page', pk=hotel_details.pk)
    else:
        form=HotelDetailsForm()

    return render(request, 'base/hotel_registration.html',{'form':form})

@login_required(login_url="login_page")
def community_registration(request):
    context = {}
    return render(request, "base/company_registration.html", context)


@login_required(login_url="login_page")
def restaurant_details(request):
    if request.method == 'POST':
        form = RestaurantDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form Data:", form.cleaned_data)
            restaurant_details=form.save()
            return redirect('restaurant_page', pk=restaurant_details.pk)
    else:
        form=RestaurantDetailsForm()

    return render(request, 'base/restaurant_registration.html',{'form':form})

@login_required(login_url="login_page")
def community(request, pk=None):
    posts = Post.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('community_list')
    else:
        form = PostForm()

    return render(request, 'base/community.html', {'posts': posts, 'form': form})

@login_required(login_url="login_page")
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('community_list')
    return redirect('community_list')

@login_required(login_url="login_page")
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    return redirect('community_list')

@login_required(login_url="login_page")
def post_content(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save to the database yet
            post.author = request.user  # Set the author to the current logged-in user
            post.save()  # Now save the post to the database
            return redirect('community_list')  # Redirect after successful submission
    else:
        form = PostForm()

    return render(request, 'base/post_content.html', {'form': form})

def community_view(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'base/community.html', {'posts': posts})


def chatbot_page(request):
    return render(request, "base/chatbot.html")
