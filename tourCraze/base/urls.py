from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page, name="login_page"), 
    path("register/", views.register_page, name="register_page"),
    path("home/", views.home_page, name="home_page"),
    path("community/", views.community_view, name="community_list"),  # Adjusted to match the view
    path("tours/<int:pk>/", views.tours_page, name="tours_page"),
    path("update_user/<int:pk>/", views.update_user, name="update_user"),  # Adjusted to match the view
    path('tours_details/', views.tours_details, name='tours_details'),
    path('hotel_details/', views.hotel_details, name='hotel_details'),
    path('company_registration/', views.community_registration, name='company_registration'),
    path('restaurant_registration/', views.restaurant_details, name='restaurant_registration'),
    path('post/', views.post_content, name='post_content'),
    path('community/<int:pk>/', views.community, name='community_display'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path("chatbot_page/", views.chatbot_page, name="chatbot_page"),
    path("maps/", views.maps, name="maps")
]




