from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User_satellite)
admin.site.register(User)
admin.site.register(Satellite)