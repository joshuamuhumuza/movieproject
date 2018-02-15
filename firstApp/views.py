from django.shortcuts import render
from .models import movie


def index(request):
    movies = movie.objects.all()
    return render(request, 'firstApp/index.html', {'movies': movies})

def about(request):
    
    return render(request, 'firstApp/upload.html')

def books(request):
    
    return render(request, 'firstApp/books.html')

def dashboard(request):
    
    return render(request, 'firstApp/dashboard.html')

def transactions(request):
    
    return render(request, 'firstApp/transactions.html')

def upload_form(request):
    
    return render(request, 'firstApp/upload_form.html')

def upload(request):
    
    return render(request, 'firstApp/upload.html')

def site_admin(request):
    return render(request, 'firstApp/site_admin.html')
# Create your views here.
