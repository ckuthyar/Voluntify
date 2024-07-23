from django import forms

class inputweb(forms.Form):
    num1=forms.IntegerField(min_value=0,max_value=99999999)
    num2=forms.IntegerField(min_value=0,max_value=99999999)
