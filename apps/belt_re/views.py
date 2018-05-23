from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import User, Author, Book, Review
import datetime, re, bcrypt

# TEST USERS
# ed@tulane.com tulane
# mp@gmail.com tulane

def index(request):
    if "user" not in request.session:
        request.session["user"] = []
        return render(request, 'belt_re/index.html')
    else:
        s = request.session["user"]
        if "logged" not in s:
            return render(request, 'belt_re/index.html')
        else:
            return render(request, 'belt_re/books.html')

def register(request):
    if User.objects.validate(request):
        User.objects.create(name=request.POST["name"], alias=request.POST["alias"], email=request.POST["email"], password=request.POST["pass1"])
        messages.success(request, "Created User, please login")
        print User.objects.all()       
    else:
        messages.error(request, "Error, check fields")
    return redirect('/belt_re/home/')

def login(request):
    users = User.objects.filter(email=request.POST["email"])
    if len(users) > 0 :
        user = users[0]
        if user.password == request.POST["pass"]:
            request.session["user"] = { "logged": user.id, "name" : user.alias }
    else:
        messages.error(request, "invalid credentials")
    return redirect("/belt_re/home/")

def logout(request):
    request.session["user"] = []
    return redirect('/belt_re/home/')

def add(request):
    return render(request, 'belt_re/add.html')

def create(request):
    if request.method == "POST":
        print request.POST
        author_name = request.POST["author1"]
        if author_name == "":
            author_name = request.POST["author2"]
        author = Author.objects.filter(name=author_name)
        if len(author) == 0:
            author = Author.objects.create(name=author_name)
        else:
            author = author[0]
       
        book_name = request.POST["bookname"]
        book = Book.objects.filter(title=book_name)
        if len(book) == 0:
            book = Book.objects.create(title=book_name, author=author)
        else:
            book = book[0]

        user = User.objects.get(id=request.session["user"]["logged"])
        
        Review.objects.create(content=request.POST["review"], rating=request.POST["rating"], user=user, book=book)
        
        return redirect('/belt_re/books/'+str(book.id))
    else:
        return redirect("belt_re/add/")

def user_page(request):
    pass

def show_book(request, book_id):
    data = {
        "book": Book.objects.get(id=book_id)
    }
    return render(request, '/belt_re/one_book.html/', data)