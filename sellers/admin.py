from django.contrib import admin

# Register your models here.
from .models import Seller
from .models import Product

class ProductInline(admin.TabularInline):
    model = Product
    extra = 3

class SellerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Seller Name', {'fields': ['first_name', 'last_name']}),
        ('Date informaion', {'fields': ['regist_date']}),
    ]
    inlines = [ProductInline]
    
    list_display = ('first_name', 'last_name', 'regist_date', 'was_published_recently')
    list_filter = ['regist_date']
    search_fields = ['regist_date']

admin.site.register(Seller, SellerAdmin)