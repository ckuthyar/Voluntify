from django import forms
class inputform(forms.Form):
    input1=forms.IntegerField(min_value=2,max_value=10)