
from django.contrib import admin
from django.urls import path
from django.urls import include
from Blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home,name='home'),
    path("blog/",include('Blogapp.urls'))
]
