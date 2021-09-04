from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.book, name='booking'),
    path('list', views.list, name='listBooking'),
    path('listData', views.listData, name='listData'),
    
    
]