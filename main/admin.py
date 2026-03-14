from django.contrib import admin
from .models import Product, ProImage, Category
# Register your models here.


admin.site.register(Category)
admin.site.register(ProImage)
admin.site.register(Product)