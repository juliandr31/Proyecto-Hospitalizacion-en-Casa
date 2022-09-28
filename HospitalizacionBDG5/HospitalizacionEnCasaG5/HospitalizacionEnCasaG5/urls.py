"""HospitalizacionEnCasaG5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from .router import router
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from Aplicacion import views

urlpatterns = [
   # path('login/', TokenObtainPairView.as_view()),
    #path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.PersonaList.as_view()),
    path('user/<int:pk>/', views.PersonaRetrieveUpdateDestroy.as_view()),
    path('medico/', views.MedicoListCreate.as_view()),
    path('medico/<int:pk>/', views.MedicoRetrieveUpdateView.as_view()),
    path('auxiliar/', views.AuxiliarListCreate.as_view()),
    path('auxiliar/<int:pk>/', views.AuxiliarRetrieveUpdateView.as_view()),
    path('familiar/', views.FamiliarListCreate.as_view()),
    path('familiar/<int:pk>/', views.FamiliarRetrieveUpdateView.as_view()),
    path('paciente/', views.PacienteListCreate.as_view()),
    path('paciente/<int:pk>/', views.PacienteRetrieveUpdateView.as_view()),
    path('enfermero/', views.EnfermeroListCreate.as_view()),
    path('enfermero/<int:pk>/', views.EnfermeroRetrieveUpdateView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
