from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Command)
admin.site.register(Response)
admin.site.register(Communication)
admin.site.register(Data)
