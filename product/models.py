from django.db import models

# Create your models here.

class Product_category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(default="default.png", upload_to="product_cat/", null=True, blank=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(default="default.png", upload_to="product/", null=True, blank=True)
    product_category = models.ForeignKey(Product_category, on_delete=models.CASCADE)
    total_views = models.IntegerField(default=0) # page view counter
    def __str__(self):
        return self.title


