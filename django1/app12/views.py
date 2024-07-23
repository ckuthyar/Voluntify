from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls.static import static

def home(request):
    result=goldmedal()
    return render(request,'app12/index.html',{'param1':result})
def goldmedal():
    f1=open("Marks.txt","r")
    s1=f1.readline()
    return s1
def image1(request):
    return render(request,'app12/index.html')

def home1(request):
    result="chandra"
    return HttpResponse(result)
