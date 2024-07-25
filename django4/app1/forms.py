from django import forms

class inputweb(forms.Form):
    name1=forms.CharField()
    date1=forms.DateField()
    activity1=forms.CharField()
    duration1=forms.IntegerField()
