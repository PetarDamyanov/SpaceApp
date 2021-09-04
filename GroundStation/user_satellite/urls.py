from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('add',views.add,name="add"),
    path('list',views.list, name="list"),
    path('register/',views.register),
    # path('login/',views.login), 
    path('logout/',views.logout, name='logout'),
]