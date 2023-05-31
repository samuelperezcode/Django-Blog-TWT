from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.login_page, name='login'),
    path('create-post/', views.create_post_page, name='create-post'),
]
