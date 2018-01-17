from django.shortcuts import render


def index(request):
    return render(request, 'firstApp/index.html')

# Create your views here.
