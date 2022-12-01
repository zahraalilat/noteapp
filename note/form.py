from django import forms

class Loginform (forms.Form):
 username=forms.CharField( max_length=150)
 password=forms.CharField(widget=forms.PasswordInput())
 #widget.....:password en ****
 date=forms.DateField()
