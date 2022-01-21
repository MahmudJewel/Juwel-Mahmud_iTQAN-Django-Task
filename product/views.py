from django.shortcuts import render
from product import models as PMODEL
# Create your views here.

def categorywise_product_view(request, pk):
    products = PMODEL.Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'product/categorywise_product.html', context)