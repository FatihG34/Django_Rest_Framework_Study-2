from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    definition = models.TextField(blank=True, null=True)

    createion_date = models.DateTimeField(auto_now_add=False)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.author}"


class Comment(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="comments")

    comments_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments_of_user')
    comment = models.TextField(blank=True, null=True)

    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    rating = models.PositiveIntegerField(
        validators=[MinValueValidator, MaxValueValidator]
    )

    def __str__(self):
        return f"{str(self.rating)}"
