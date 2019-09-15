from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.core.handlers.wsgi import WSGIRequest
import json


# Create your views here.

def index(request, year):
    test(request)
    return HttpResponse("Hello, world. You're at the polls index.")


def index_1(request):
    return HttpResponse('test')


def index_2(request, page_number):
    print(page_number)
    return HttpResponse('page number is {0}'.format(page_number))


def index_name(request, name):
    return HttpResponse('name is {0}'.format(name))


def rev_parse(request):
    return HttpResponse("Your requested URL is {0}".format(reverse("askname")))


def test(request):
    # print(type(request))  # 打印出request的类型
    print(request.__dict__)  # 打印出request的header详细信息
    # 循环打印出每一个键值对
    # for k, v in request.environ.items():
    # print(k, v)
