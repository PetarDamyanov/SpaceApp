from user_satellite.models import User_satellite
from django.shortcuts import redirect

def login_required(method):
    def inner_method(request, *args, **kwargs):
        if request.session.get("username"):
            return method(request ,*args, **kwargs)
        else:
            return redirect("login")
    return inner_method