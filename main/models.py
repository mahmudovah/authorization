from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    

class ProImage(models.Model):
    image = models.ImageField(upload_to="images/")
    

class Product(models.Model):
    images = models.ManyToManyField(ProImage)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    discount_type = (
        ('gr', 'gram'),
        ('kg', 'kilogram'),
        ('ml', 'mill'),
        ('l', 'litr'),
        ('pc', 'dona')
        )
    discount = models.CharField(max_length=10)
    status = models.BooleanField()

    def __str__(self):
        return self.title
    
