from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re

class UserManager(models.Manager):
    def validate(self, request):
        valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if request.method != "POST":
            valid = False
        for key in request.POST:
            if request.POST[key] == "":
                valid = False
                messages.error(request, "{} need to be filled in".format(key))
        if request.POST["pass1"] != request.POST["pass2"]:
            valid = False
            messages.error(request, "password must match confirmation password")
        if not EMAIL_REGEX.match(request.POST["email"]):
            valid = False
            messages.add_message(request, message.INFO, "Please enter a valid email")
        return valid            

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, default='anon')
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="has_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Review(models.Model):
    book = models.ForeignKey(Book, related_name="reviews")
    user = models.ForeignKey(User, related_name="reviews")
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)