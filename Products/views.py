from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Shambhoo')


def new(request):
    return HttpResponse('New Page Chant Har Har Mahadeva!')
