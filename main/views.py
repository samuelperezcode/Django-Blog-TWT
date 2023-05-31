from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, PostForm
from .models import Post


@login_required(login_url="/login/")
def home_page(request):
    posts = Post.objects.all()
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
        return redirect("home")

    return render(request, "main/home.html", {"posts": posts})


@login_required(login_url="/login/")
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()

        return render(request, "main/create_post.html", {"form": form})


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "registration/sign_up.html", {"form": form})
