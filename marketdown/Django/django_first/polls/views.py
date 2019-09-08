from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index_1(request):
    print(type(request))
    print(request.__dict__)
    return HttpResponse('test')
