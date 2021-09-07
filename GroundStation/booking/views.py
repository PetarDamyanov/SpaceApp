from os import stat
from user_satellite.views import satellite
from django.http import HttpResponse, request
from .models import Booking, Data
from user_satellite.models import *
from django import forms
from django.forms import ModelForm, widgets
from utls.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.core import serializers
from utls.file_manipulation import *
import json
import time

def index(request):
    return HttpResponse("Hello, world. You're at the satellite .")

holdFile = ''

@login_required
def book(request):
    class BookingForm(forms.Form):
        sat_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'})) #User_satellite.objects.filter(users_id=request.session.get('id')).all().values_list('satellite_id')
        start_time = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}))
        end_time = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}))

    form = BookingForm(request.POST or None)
    if form.is_valid():
        # sat=User_satellite.objects.get(id=form.data['satellite'])
        # book = Booking(user_id=User.objects.get(id=request.session.get('id')),satellite_id=Satellite.objects.get(norad_id=sat.satellite_id) ,begin=form.data["start_time"],end=form.data["end_time"])
        # book.save()
        fields={'norad_id':form['sat_id'].value(),'start_time':form['start_time'].value(),'end_time':form['end_time'].value()}
        bookToJson=json.dumps(fields)
        fName = f"API/{fields['norad_id']}_{time.time()}_out.json"
        try:
            create_file(fName)
            write_file(fName,bookToJson)
            holdFile = fName
        except FileExistsError:
            write_file(fName,bookToJson)
            
    context = {
        'form':form, 'username': request.session.get('username'),
         'satellite':User_satellite.objects.filter(users_id=request.session.get('id')).all()
            }
    return render(request,"booking/booking.html", context)

@login_required
def list(request):
    user = get_object_or_404(User, id=request.session.get('id'))
    # return HttpResponse(Booking.objects.filter(user_id=user).all())
    return render(request, 'booking/list.html', {'username':request.session.get("username"),'bookings': Booking.objects.filter(user_id=user).all()})

@login_required
def listData(request):
    user = get_object_or_404(User, id=request.session.get('id'))
    books = Booking.objects.filter(user_id=user).all()
    # return HttpResponse(Data.objects.filter(booking_id__in= books).all())
    return render(request, 'data/list.html', {'username':request.session.get("username"),'datas': Data.objects.filter(booking_id__in= books).all()})

@login_required
def dataView(request):
    user = get_object_or_404(User, id=request.session.get('id'))
    books = Booking.objects.filter(user_id=user).first()
    # return HttpResponse(Data.objects.filter(booking_id=books).first())
    return render(request, 'data/data.html', {'username':request.session.get("username"),'data': Data.objects.filter(booking_id=books).first()})

def addData(request):
    fIn=holdFile[:-3:]
    fIn = f"{fIn}in"
    # while(check_file(fIn)):
        #read file and add to data
        # data = Data(user_id = read userid form file, booking_id = read from file, ...)
    delete_file(fIn)
    delete_file(holdFile)
