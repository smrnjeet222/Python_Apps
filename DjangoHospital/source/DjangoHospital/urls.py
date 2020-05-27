"""DjangoHospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import homeView , contactView, aboutView
from doctors.views import doctorDetailView, doctorCreateView


urlpatterns = [
    path('', homeView, name='home'),
    path('about/', aboutView, name='about'),
    path('contact/', contactView, name='contact'),
    path('doctor/', doctorDetailView),
    path('create/', doctorCreateView),
    path('admin/', admin.site.urls),

]
