from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print('im home')
    return HttpResponse('home')

def hotel(request):
    print('im hotel')
    return HttpResponse('hotel')
