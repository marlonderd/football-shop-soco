from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255) # nama item
    price = models.IntegerField() # harga item
    description = models.TextField() # deskripsi item
    thumbnail = models.URLField(blank=True, null=True) # link gambar
    category = models.CharField(max_length=100) # kategori item
    is_featured = models.BooleanField(default=False) # status item
    
    def __str__(self):
        return self.title
# Create your models here.
