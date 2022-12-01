"""notetaken URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from note.views import *
from django.conf import settings
from django.conf.urls.static import static
 #from import settings
urlpatterns = [

    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('createnote/',createnote,name='createnote'),
    path('createnotetemp/',createnotetemp,name='createnotetemp'),
    path('updatenote/<int:id>/',updatenote,name='updatenote'),
    path('updatenotepost/<int:id>/',updatenotepost,name='updatenotepost'),
    path('deletenote/<int:id>/',deletenote,name='deletenote'),
    path('archivenotes/',archive,name='archive'),
    path('restore/<int:id>/',restore,name='restore'),
    path('signup/',sign,name='sign up'),
    path('userregister/',userregisterpost,name='createuser'),
    path('login/',login , name='login'),
    path('logintemp/',loginpost,name='logintemp'),
    #path('notes/',include('note.urls.py')),
    path('logout/',logoutuser,name='logout'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
