from django.shortcuts import render
from app2.forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            limit=data1.get("num1")
            result=factorial2(limit)
            return render(request,'app2/index.html',{'param1':result,"form":form1})
    else:
        form1=inputweb()
    return render(request,'app2/index.html',{"form":form1})

def factorial1(n):
    fact1=1
    for i in range(n,0,-1):
        fact1=fact1*i
    return fact1
def factorial2(n):
    list1=[]
    for i in range(2,n+1,1):
        list1.append(factorial1(i))
    return list1
