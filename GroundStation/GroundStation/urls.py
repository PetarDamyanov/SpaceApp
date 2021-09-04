from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('',include("user_satellite.urls")),
    path('booking/',include("booking.urls")),
    # path('admin/', admin.site.urls),
    
]
