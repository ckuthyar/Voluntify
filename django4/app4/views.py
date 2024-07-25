from django.shortcuts import render
from app4.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'app4/index.html',{'param1':"Success","form":form1})
    else:
        form1=inputform()
    return render(request,'app4/index.html',{"form":form1})

def factorial1(n):
    fact1=1
    for i in range(n,0,-1):
        fact1=fact1*i
    return fact1
