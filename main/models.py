from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('clothes', 'Clothes'),
        ('shoes', 'Shoes'),
        ('accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=255) # nama item
    price = models.IntegerField() # harga item
    description = models.TextField() # deskripsi item
    thumbnail = models.URLField(blank=True, null=True) # link gambar
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Product') # kategori item
    is_featured = models.BooleanField(default=False) # status item
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()
# Create your models here.
