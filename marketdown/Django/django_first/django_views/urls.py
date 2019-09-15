from django.urls import path, re_path

from . import views

urlpatterns = [
    path('teacher/', views.teacher, name='teacher'),
    path('v2_exp/', views.v2_exception, name='v2_exception'),
]
