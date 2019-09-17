from django.shortcuts import render, render_to_response
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
import os

# Create your views here.

def teacher(request):
    return HttpResponse('teacher')


def v2_exception(request):
    # raise Http404
    return HttpResponse('v2')


def v10_1(request):
    return HttpResponseRedirect("/views/v11")


def v10_2(request):
    return HttpResponseRedirect(reverse("v11"))


def v11(request):
    return HttpResponse("哈哈，只是v11的访问返回呀")


def v8_get(request):
    rst = ''
    for k, v in request.GET.items():
        rst += k + "-->" + v
        rst += ","
    return HttpResponse("Get values of Request is {0}".format(rst))


def v9_get(request):
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return render_to_response("for_post.html")
