from django.shortcuts import render
from app6.forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            n=data1.get("num1")
            result=showWebsites("websites1.txt")
            return render(request,'app6/index.html',{'param1':result,'param2':n,"form":form1})
    else:
        form1=inputweb()
    return render(request,'app6/index.html',{"form":form1})

def showWebsites(fname):
    f1=open(fname,"r")
    list1=[]
    for i in range(0,5,1):
        s1=f1.readline().replace("\n","")
        list1.append(s1)
    return list1

