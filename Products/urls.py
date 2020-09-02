from django.urls import path
from . import views

app_name = 'Products'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='newpage'),
    path('customer/', views.customer, name='customer'),


]
