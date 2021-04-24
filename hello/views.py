from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Só nas internet hein filhão")
