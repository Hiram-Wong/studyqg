from django.urls import path

from . import views

# 定义接口
urlpatterns = [
    path('', views.index, name="index"),
    path('banner', views.banner, name="banner"),
    path('search', views.search, name="search"),
    path('log', views.log, name="log"),
    path('id', views.id, name="id"),
    path('basic', views.basic, name="basic"),
]
