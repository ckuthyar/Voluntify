from django import forms

class inputweb(forms.Form):
    event1=forms.CharField(label="Enter event name")
    y1=forms.IntegerField()
    M1=forms.IntegerField()
    d1=forms.IntegerField()
