from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from home import views

urlpatterns = [
    path('', views.home_view, name='hm'),
    path('home', views.product_home_view, name='home'),
    
    path('login', LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='home/logout.html'), name='logout'),

    path('afterlogin', views.afterlogin_view, name='afterlogin'),

]