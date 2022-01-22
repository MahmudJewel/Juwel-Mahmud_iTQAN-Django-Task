from django.shortcuts import render
from product import models as PMODEL
from django.db.models import F # for page view counter 

# Create your views here.

def categorywise_product_view(request, pk):
    products = PMODEL.Product.objects.filter(product_category=pk)
    category = PMODEL.Product_category.objects.get(id=pk)
    context = {
        'products':products,
        'category':category,
    }
    return render(request, 'product/categorywise_product.html', context)

def single_product_view(request, pk):
    product = PMODEL.Product.objects.get(id=pk)
    
    # page view counter 
    product.total_views = F('total_views')+1
    product.save()
    
    context = {
        'product': product,
    }
    return render(request, 'product/single_product_view.html', context)