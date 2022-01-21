from django.urls import path, include
from product import views

urlpatterns = [
    path('/<int:pk>/product', views.categorywise_product_view, name=''),
]