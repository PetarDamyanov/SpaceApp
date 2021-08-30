from django.forms.forms import Form
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from .models import User, Satellite, User_satellite
from django.urls import reverse_lazy
import datetime
from utls.salt import create_salt
from utls.hash_pass import hash_password

def index(request):
    return HttpResponse("Hello, world. You're at the satellite - user .")

#=========================================================================
#                                    User
class UserRegister(ModelForm):
    class Meta:
        model = User
        widgets = {'password': forms.PasswordInput()}
        fields = ['username', 'password']
        def get_get_success_url(self, **kwargs):
            return reverse_lazy('login')

def register(request):
    form = UserRegister(request.POST or None)
    if form.is_valid():
        salt = create_salt()
        user = User(username=form.data['username'],password=hash_password(form.data["password"],salt),salt=salt)
        user.save()
    context = {
        'form':form
    }
    return render(request,"users/register.html", context)

def login(request):
    form = UserRegister(request.POST or None)
    if form.is_valid():
        try:
            # check if user is in db
            user = User.objects.get(username=form.data['username'])
            try:
                # check if password is correct
               hash_password(form.data['password'], user.getSalt()) == user.getPass()
            except:
                return HttpResponse(f"Wrong password")
            request.session['id'] = user.id
            request.session['username']=user.username
            # next line was for fixing salt and pass hashing
            # return HttpResponse(f"{user}")
            # the next line was used for testing and fixing the session
            # return HttpResponse(f'{request.session.get("id")}, {request.session.get("username")}')
        except User.DoesNotExist:
            return HttpResponse("NO such user")
    context = {
        'form':form
    }
    return render(request,"users/login.html", context)

#=========================================================================
#                                   Satellite
class AddSatellite(ModelForm):
    class Meta:
        model = Satellite
        fields = ['norad_id', 'frequency','protocol']

def index(request):
    return HttpResponse("Hello, world. You're at the satellite .")

def satellite(request, norad_id):
    return HttpResponse(f"You are looing at {norad_id}")

def add(request):
    form = AddSatellite(request.POST or None)
    if form.is_valid():
        form.save()
        sat = Satellite.objects.get(norad_id=form.data['norad_id'])
        user_satellite = User_satellite(users_id=User.objects.get(id=request.session.get('id')),satellite_id=sat)
        user_satellite.save()
    context = {
        'form':form, 'username': request.session.get('username')
    }
    return render(request,"satellite/register.html", context)

def list(request):
    user = get_object_or_404(User, id=request.session.get('id'))
    return render(request, 'satellite/list.html', {'username':request.session.get("username"),'satellites': User_satellite.objects.filter(users_id=user).all()})