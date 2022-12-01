from unicodedata import name
from django.contrib import admin
from django.urls import path
from note.views import *
urlpatterns =[
    path('createnote/',createnote,name='createnote'),
    path('createnotetemp/',createnotetemp,name='createnotetemp'),
    path('updatenote/<int:id>/',updatenote,name='updatenote'),
    path('updatenotepost/<int:id>/',updatenotepost,name='updatenotepost'),
    path('deletenote/<int:id>/',deletenote,name='deletenote'),
    path('archivenotes/',archive,name='archive'),
    path('restore/<int:id>/',restore,name='restore'),

] 