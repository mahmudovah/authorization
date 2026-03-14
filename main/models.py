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
    stock = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
   
    unit_type_ch = (
        ('gr', 'gram'),
        ('kg', 'kilogram'),
        ('ml', 'mill'),
        ('l', 'litr'),
        ('pc', 'dona'))
    unit_type = models.CharField(max_length=10, choices=unit_type_ch)
   
    discount_type_ch = (
        ('percent', 'foizli'),
        ('flex', 'aniq'))
    discount_type = models.CharField(max_length=15, choices=discount_type_ch)
    discount = models.IntegerField(default=0)

    def finally_price(self):
        if self.discount:
            if self.discount_type == 'percent':
                return self.price - (self.price / 100 * self.discount)
            return self.price - self.discount
        return self.price

    def __str__(self):
        return self.title