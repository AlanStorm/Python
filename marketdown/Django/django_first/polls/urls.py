from django.urls import path, re_path

from . import views

urlpatterns = [
    path('<int:year>/', views.index, name='index'),
    path('index_1/', views.index_1, name='index_1'),
    re_path(r'index_2/(?:page-(?P<page_number>\d+)/)?$', views.index_2, name='index_2'),
]
