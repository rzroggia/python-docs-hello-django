from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    name = input("Nome?")
    return HttpResponse("Bien venido", name)
