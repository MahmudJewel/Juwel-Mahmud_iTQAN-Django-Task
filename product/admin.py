from django.contrib import admin
from product import models
# Register your models here.

admin.site.register(models.Product)
admin.site.register(models.Product_category)