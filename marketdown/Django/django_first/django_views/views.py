from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def teacher(request):
    return HttpResponse('teacher')


def v2_exception(request):
    return HttpResponse('v2')


def v10_1(request):
    return HttpResponseRedirect("/views/v11")


def v10_2(request):
    return HttpResponseRedirect(reverse("v11"))


def v11(request):
    return HttpResponse("哈哈，只是v11的访问返回呀")
