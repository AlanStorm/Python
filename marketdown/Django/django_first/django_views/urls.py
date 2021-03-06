from django.urls import path, re_path

from . import views

urlpatterns = [
    path('teacher/', views.teacher, name='teacher'),
    path('v2_exp/', views.v2_exception, name='v2_exp'),

    path('v10_1/', views.v10_1),
    path('v10_2/', views.v10_2),
    path('v11/', views.v11, name="v11"),
    path("v8_get/", views.v8_get, name='v8_get'),
    path("v9_get/", views.v9_get, name='v9_get'),
    path("v9_post/", views.v9_post, name='v9_post'),
    path("render_test/", views.render_test),
    path("render2_test/", views.render2_test),
    path("render3_test/", views.render3_test),
    path("render4_test/", views.render4_test),
    path("get404/", views.get404),
]
