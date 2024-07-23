from django.shortcuts import render
from app5.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            result=cube(n1)
            return render(request,'app5/index.html',{'form':form1,'param1':result})
    else:
        form1=inputform()
    return render(request,'app5/index.html',{'form':form1})

def cube(n1):
    return n1*n1*n1