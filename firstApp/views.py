from django.shortcuts import render
from .models import movie


def index(request):
    movies = movie.objects.all()
    return render(request, 'firstApp/index.html', {'movies': movies})

# Create your views here.
