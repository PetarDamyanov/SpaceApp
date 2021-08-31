from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.book, name='booking'),
    path('list', views.list, name='list'),
    path('listData', views.listData, name='list'),
    
    
]