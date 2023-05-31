from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path("post/", views.create_post, name="create-post"),
]
