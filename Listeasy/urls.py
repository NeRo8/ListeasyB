"""Listeasy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from django.conf import settings
from django.conf.urls.static import static

from .views import FacebookLogin, GoogleLogin

schema_view = get_swagger_view(title='Listeasy')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include('rest_auth.urls')),
    url(r'^api/v1/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/facebook/$', FacebookLogin.as_view()),
    url(r'^api/v1/google/$', GoogleLogin.as_view()),
    url(r'^api/v1/profile/', include('Profiles.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api-docs', schema_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
