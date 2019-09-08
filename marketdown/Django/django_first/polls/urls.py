from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_1', views.index_1, name='index_1')
]
