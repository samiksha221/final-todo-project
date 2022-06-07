"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from .views import TaskViewset
from rest_framework import routers
routers=routers.DefaultRouter()
routers.register('Task',TaskViewset)
from rest_framework_simplejwt.views import TokenVerifyView,TokenRefreshView,TokenObtainPairView

urlpatterns = [
    path('',include(routers.urls)),
    path('api-auth/',include('rest_framework.urls')),
    path('token/',TokenObtainPairView.as_view()),
    path('refreshtoken/',TokenRefreshView.as_view()),
    path('verifytoken/',TokenVerifyView.as_view()),

]
