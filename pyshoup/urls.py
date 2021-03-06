"""pyshoup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# products
from Products import views


# dprojx/urls.py
from django.conf.urls import url, include
from resit import views
# pyshoup views
from . import views


urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('products/', include('Products.urls')),
    path('resit/', include('resit.urls')),
    #     url(r'^$', views.Loginindex, name='Loginindex'),
    #     url(r'^special/', views.special, name='special'),
    #     url(r'^logout/$', views.user_logout, name='logout'),
    # ]

    # urlpatterns = [
    #     path('admin/', admin.site.urls),
]
