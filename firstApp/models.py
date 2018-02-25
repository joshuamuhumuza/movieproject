from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    TYPE = (
        ('BK', 'Book'),
        ('AU', 'Audio'),
    )
    type = models.CharField(max_length=6, choices = TYPE, default = "Book")
    genre = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=13)
    sales = models.IntegerField(default = 0)
    publish_date = models.DateField(blank=True, null=True)
    description = models.TextField(default="")
    price = models.IntegerField(default=0)
    book_pic = models.ImageField(upload_to = 'HozyBookApp/static/pic_folder/', default = 'pic_folder/None/no-img.jpg')        
    audio_file =  models.FileField(upload_to = 'firstApp/audioFiles', default = "", null = True, blank = True)
    
class Transaction(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    buyer = models.CharField(max_length=100)
    transaction_id = models.AutoField(max_length=90, primary_key = True)
    time = models.TimeField(auto_now_add=True)
    purchase_date = models.DateField(auto_now_add=True)

class User(models.Model):
    username = models.CharField(max_length=50)
    PREVILAGES = (
        ('SU', 'Super Admin'),
        ('ED', 'Editor'),
    )
    previlages = models.CharField(choices = PREVILAGES, max_length=10)
    activation = models.BooleanField()
