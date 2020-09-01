# dappx/urls.py
from django.conf.urls import url
from django.urls import path
from . import views
# SET THE NAMESPACE!
app_name = 'resit'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    path('', views.Index, name='Index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
]
