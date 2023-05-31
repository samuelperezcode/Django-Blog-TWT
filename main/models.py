from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
