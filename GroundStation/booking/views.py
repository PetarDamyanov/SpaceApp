from user_satellite.views import satellite
from django.http import HttpResponse, request
from .models import Booking, Data
from user_satellite.models import *
from django import forms
from django.forms import ModelForm, widgets
from utls.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404



def index(request):
    return HttpResponse("Hello, world. You're at the satellite .")

@login_required
def book(request):
    class BookingForm(forms.Form):
        satellite = forms.ModelMultipleChoiceField(queryset=User_satellite.objects.filter(users_id=request.session.get('id')).all()) #User_satellite.objects.filter(users_id=request.session.get('id')).all().values_list('satellite_id')
        start_time = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}))
        end_time = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}))

    form = BookingForm(request.POST or None)
    if form.is_valid():
        # return HttpResponse(User_satellite.objects.filter(id=form.data['satellite']).get())
        sat=User_satellite.objects.get(id=form.data['satellite'])
        # return HttpResponse(sat.satellite_id)
        book = Booking(user_id=User.objects.get(id=request.session.get('id')),satellite_id=Satellite.objects.get(norad_id=sat.satellite_id) ,begin=form.data["start_time"],end=form.data["end_time"])
        book.save()
    context = {
        'form':form, 'username': request.session.get('username')
    }
    return render(request,"booking/booking.html", context)