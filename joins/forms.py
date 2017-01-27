from django import forms
from .models import Join



#        [ This is the default Django form ]
#Django knows to look for forms.py in your app folder
class EmailForm(forms.Form):
#You can add Fields to a form that are not required to be fill out like this
    name = forms.CharField(required=False)
#Fields left empty will be required Fields by defualt
    email = forms.EmailField()

#        [ This is the model form ]
class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ['email',]
        #exclude = ['timestamp','updated','ip_address']
# You either need to state the fields you want filled out with fields=['',''] or exclude the ones
# you don't want to be  in the form fields














