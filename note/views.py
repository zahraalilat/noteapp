from django.shortcuts import render, redirect
from note.models import note
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as loginD,logout
from .form import *
# Create your views here.
def home(request):
     context={}
     if request.user.is_authenticated:
          currentuser=request.user
          notes =note.objects.filter(owner__id=currentuser.id,archive=False)#.order_by()
 
          context={
          'notes':notes
           }
          print(currentuser)
     return render(request,'home.html',context)
 

def createnotetemp (request):
 return render(request ,'createnote.html')


def createnote (request):
 notes = note.objects.all()
 title = request.POST.get('title')
 content = request.POST.get('content')
 
 notes.update_or_create(title=title, defaults={'content':content},archive=False,owner=request.user)
 return redirect('home')

def updatenote(request,id):
    notes = note.objects.filter(id=id).first()
    context={
    'title':notes.title,
    'content':notes.content,
    'id':notes.id,
         }
    return render (request,'update.html',context)
def updatenotepost (request, id):
     notes = note.objects.filter(id=id)
     title = request.POST.get('title')
     content = request.POST.get('content')
     notes.update(title=title,content=content) 
     return redirect('home')

def deletenote(request,id):
    notes = note.objects.filter(id=id)
    notes.update(archive=True)
    #archive + deletenote
    #notes.delete()
    return redirect('home') 
def archive(request):
     notee=note.objects.filter(archive=True)
     msg=''
     if not notee:
          msg='There are no archived notes'
     
     context={
     'notee':notee,
     'msg': msg
      }
     return render(request,'archive.html',context)
def restore(request, id):
      notes = note.objects.filter(id=id)
      notes.update(archive=False)
      return redirect('archive')
def sign(request):
     return render (request,'signup.html')
def userregisterpost(request):
     #retreive data
     email=request.POST.get('Email')
     password=request.POST.get('Password')
     username=request.POST.get('User name')
     #create user
     user = User.objects
     user.create_user(username=username,email=email,password=password)
    
     for i in user.all() :
          print(i.password)
     return redirect('home')
#login user
def login(request):
     login_form =Loginform()
     print(login_form)
     context={
         'loginform':login_form,
     }
     return render(request, 'login.html',context) 
def loginpost (request):
      password=request.POST.get('Password')
      username=request.POST.get('User name')
#if loginform is valid
#if loginform.is_valid():
#or request.data["username"]...backend séparée du front
      user=authenticate(username=username,password=password)
      if user is not None:
          username=user.get_username()
          loginD(request, user)
          context={
               'username':username,
          }
          return render (request , 'welcome.html',context)
      else:
          return redirect ('login')
def logoutuser(request):
     logout(request)
     return redirect('home')

