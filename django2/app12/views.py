from django.shortcuts import render
from app12.forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            n1=data1.get("num1")
            n2=data1.get("num2")
            result=calc1(n1,n2)
            return render(request,'app12/index.html',{'param1':result,"form":form1})
    else:
        form1=inputweb()
    return render(request,'app12/index.html',{"form":form1})

def calc1(n1,n2):
    list1=[]
    s1=n1+n2
    m1=n1-n2
    p1=n1*n2
    d1=n1/n2
    list1.append(s1)
    list1.append(m1)
    list1.append(p1)
    list1.append(d1)
    return list1
