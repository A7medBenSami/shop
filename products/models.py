from pickle import TRUE
from unicodedata import category
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField 

class Product(models.Model):
    category = (
        ('Mobile','Mobile'),
        ('Computer','Computer'),
        ('Vape', 'Vape')
    )
    
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=9, decimal_places=3)
    description = RichTextField()
    mini_description = RichTextField()
    category = models.CharField(max_length=20,choices=category)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_active = models.BooleanField(default=TRUE)
    adding_date = models.DateTimeField(default=datetime.now)
    stock = models.IntegerField()


    def __str__(self):
        return self.name
