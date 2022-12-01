from contextlib import nullcontext
from django.db import models
from django.contrib.auth.models import User,AbstractUser

class note (models.Model):
  title = models.CharField( max_length=150)
  content =models.TextField('content')
  createdat =models.DateTimeField( auto_now=True)
  updatedat=models.DateTimeField( auto_now_add=True)
  archive=models.BooleanField(auto_created=False)
  #many to one relation 
  owner=models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self):
      return self.title 

  #custom user personalisé
#class CustomUser(AbsractUser):
 # username=
  #email=

  #USERNAME_FIELD=email .... email obligatoire 
     
 #is active is stuff is admin