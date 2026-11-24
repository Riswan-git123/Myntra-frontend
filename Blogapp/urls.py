
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("contact/",Contact,name='contact'),
    path("about/",About,name='about')
    
]
