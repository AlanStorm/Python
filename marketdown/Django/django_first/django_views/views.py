from django.shortcuts import render, render_to_response
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views import defaults
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


def v9_post(request):
    rst = ''
    for k, v in request.POST.items():
        rst += k + '-->' + v
        rst += ","

    return HttpResponse("Get value of POST is {0}".format(rst))


def render_test(request):
    # 环境变量
    # c = dict()

    rsp = render(request, 'render.html')

    return rsp


def render2_test(request):
    # 环境变量
    c = dict()

    c["name"] = "haha"
    c["name1"] = "haha1"
    c["name2"] = "haha2"

    rsp = render(request, 'render2.html', context=c)
    return rsp


def render3_test(request):
    # 得到模板
    t = loader.get_template('render2.html')
    print(type(t))

    r = t.render(context={"name": "测试"})
    print(type(r))

    return HttpResponse(r)


def render4_test(request):
    rsp = render_to_response("render2.html", context={"name": "老师看来是"})

    return rsp


def get404(request):
    return defaults.page_not_found(request, Exception)
