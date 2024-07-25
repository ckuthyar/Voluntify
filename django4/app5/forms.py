from django import forms
from app5.models import users

class inputform(forms.ModelForm):
    class Meta:
        model=users
        fields=['name1','date1','activity1','duration1']
