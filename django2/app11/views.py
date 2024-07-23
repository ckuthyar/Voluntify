from django.shortcuts import render
from app11.forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            n1=data1.get("num1")
            n2=data1.get("num2")
            result=calc1(n1,n2)
            return render(request,'app11/index.html',{'param1':result,"form":form1})
    else:
        form1=inputweb()
    return render(request,'app11/index.html',{"form":form1})

def factorial1(n):
    fact1=1
    for i in range(n,0,-1):
        fact1=fact1*i
    return fact1
def calc1(n1,n2):
    p1=n1*n2
    return p1