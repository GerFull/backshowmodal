from django.contrib import admin
from django.urls import re_path, include

#from django.conf.urls import url, include

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^',include('ShowModalApp.urls'))
]
