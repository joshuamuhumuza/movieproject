from django.shortcuts import render, redirect
from firstApp.models import Book

def books(request):
    book = Book.objects.all()



    
    return render(request, 'firstApp/books.html',{'books':book})