from django.shortcuts import render
from app3.forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            n=data1.get("num1")
            result=5
            return render(request,'app3/index.html',{'param1':result,"form":form1})
    else:
        form1=inputweb()
    return render(request,'app3/index.html',{"form":form1})

