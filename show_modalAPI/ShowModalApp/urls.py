"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path
from ShowModalApp import views

from django.conf.urls.static import static 

from django.conf import settings 

urlpatterns = [
    re_path(r'^api/objModel/$', views.objModel_list),
    re_path(r'^api/objModel/(?P<pk>[[a-zA-Zа-яА-Я0-9]+)$', views.objModel_detail),

    re_path(r'^api/objModel/savefile',views.SaveFile) 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
