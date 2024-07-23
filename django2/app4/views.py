from django.shortcuts import render
from app4.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            result=square(n1)
        return render(request,"app4/index.html",{'form':form1,'param1':result})
    else:
        form1=inputform()  
    return render(request,"app4/index.html",{'form':form1})

def square(n1):
    return n1*n1