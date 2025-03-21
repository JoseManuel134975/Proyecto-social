"""
URL configuration for proyecto_social project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from usuarios_app.views import salir, registro, index
from tests_app.views import crear_test, agregar_pregunta, ver_preguntas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('salir/', salir, name='salir'),
    path('registro/', registro, name='registro'),
    path('index/', index, name="index"),
    path('crear_test/', crear_test, name="crear_test"),
    path('agregar_pregunta/<int:pk>', agregar_pregunta, name="agregar_pregunta"),
    path('ver_preguntas/<int:pk>', ver_preguntas, name="ver_preguntas"),
]
