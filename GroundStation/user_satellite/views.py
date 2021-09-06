import user_satellite
from django.forms.forms import Form
from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.forms import ModelForm
from .models import User, Satellite, User_satellite
from django.urls import reverse_lazy
import datetime
from utls.salt import create_salt
from utls.hash_pass import hash_password
from utls.decorators import login_required

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
            return reverse_lazy(' ')

def register(request):
    form = UserRegister(request.POST or None)
    if form.is_valid():
        try:
            User.objects.get(username=form.data['username'])
            return HttpResponse("User is taken")
        except:
            salt = create_salt()
            user = User(username=form.data['username'],password=hash_password(form.data["password"],salt),salt=salt)
            user.save()
            return redirect('login')
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
            #    return render(request,"user_satellite/list.html")
            except:
                return HttpResponse(f"Wrong password")
            request.session['id'] = user.id
            request.session['username']=user.username
            return redirect('list')
            # next line was for fixing salt and pass hashing
            # return HttpResponse(f"{user}")
            # the next line was used for testing and fixing the session
            # return HttpResponse(f'{request.session.get("id")}, {request.session.get("username")}')
        except User.DoesNotExist:
            return HttpResponse("NO such user")
    context = {
        'form':form,
        'sat':Satellite.objects.all()
    }
    return render(request,"users/login.html", context)

def logout(request):
    del request.session["username"]
    del request.session["id"]
    return redirect("login")

#=========================================================================
#                                   Satellite
class AddSatellite(ModelForm):
    class Meta:
        model = Satellite
        fields = ['norad_id','name','frequency','protocol','sma','inc','raan','aop','ecc','ta']
        

def index(request):
    return HttpResponse("Hello, world. You're at the satellite .")

def satellite(request, norad_id):
    return HttpResponse(f"You are looing at {norad_id}")

@login_required
def add(request):
    form = AddSatellite(request.POST or None)
    if form.is_valid():
        form.save()
        sat = Satellite.objects.get(norad_id=form.data['norad_id'])
        user_satellite = User_satellite(users_id=User.objects.get(id=request.session.get('id')),satellite_id=sat)
        user_satellite.save()
        return redirect('list')
    context = {
        'form':form, 'username': request.session.get('username')
    }
    return render(request,"satellite/add.html", context)

@login_required
def list(request):
    user = get_object_or_404(User, id=request.session.get('id'))
    return render(request, 'satellite/list.html', {'username':request.session.get("username"),'satellites': User_satellite.objects.filter(users_id=user).all()})