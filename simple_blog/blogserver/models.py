from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # user = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
