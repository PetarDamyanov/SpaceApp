from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add',views.add,name="add"),
    path('list',views.list, name="list"),
    path('register/',views.register),
    path('login/',views.login), 
]