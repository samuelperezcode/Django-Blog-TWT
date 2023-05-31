from django.shortcuts import render


def home_page(request):
    return render(request, 'main/home.html')


def login_page(request):
    return render(request, 'main/login.html')


def create_post_page(request):
    return render(request, 'main/create_post.html')
