from django.shortcuts import render
from app7.forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            web1=data1.get("web1")
            result=showWebsites2("websites2.txt")
            return render(request,'app7/index.html',{'param1':result,"form":form1})
    else:
        form1=inputweb()
    return render(request,'app7/index.html',{"form":form1})

def showWebsites2(fname):
    f1=open(fname,"r")
    list1=[]
    list2=[]
    list3=[]
    for i in range(0,5,1):
        s1=f1.readline().replace("\n","")
        temp=s1.split(",")
        list1.append(temp[0])
        list2.append(temp[1])
        list3.append(temp[2])
    return zip(list1,list2,list3)