import datetime

from django.db import models
from django.utils.timezone import now
from django.contrib import admin

# Create your models here.

class Seller(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    contact_number = models.CharField(max_length = 30)
    regist_date = models.DateTimeField('date published', default = now)

    def __str__(self):
        return (self.first_name + " " + self.last_name)
    
    @admin.display(
        boolean = True,
        ordering = 'regist_date',
        description = 'Published recently?',
    )
    
    def was_published_recently(self):
        cur_time = now()
        return (cur_time - datetime.timedelta(days = 1)) <= self.regist_date <= cur_time
    

class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete = models.CASCADE)
    item_name = models.CharField(max_length = 100)
    item_quantity = models.IntegerField()
    item_price = models.DecimalField(max_digits = 9, decimal_places = 2)
    item_description = models.TextField()
    
    def __str__(self):
        return self.item_name