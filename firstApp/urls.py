from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload_form/', views.upload_form, name='upload_form'),
    path('books/', views.books, name='books'),
    path('transactions/', views.transactions, name='transactions'),
    path('site_admin/', views.site_admin, name='site_admin'),

]    