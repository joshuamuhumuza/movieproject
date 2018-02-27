from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload_book/', views.upload_book, name='upload_book'),
    path('books/', views.books, name='books'),
    path('transactions/', views.transactions, name='transactions'),
    path('site_admin/', views.site_admin, name='site_admin'),
    
    
    

]    