from django.shortcuts import render
from app7.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            result=quadruple(n1)
            return render(request,'app7/index.html',{'param1':result,'form':form1})
    else:
        form1=inputform()
    return render(request,'app7/index.html',{'form':form1})

def quadruple(n1):
    return n1**4