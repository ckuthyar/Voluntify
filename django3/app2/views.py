from django.shortcuts import render
from app2.forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            event1=data1.get("event1")
            y1=data1.get("y1")
            M1=data1.get("M1")
            d1=data1.get("d1")
            result=daysleft(y1,M1,d1)
            return render(request,'app2/index.html',{'param1':result,'param2':event1,"form":form1})
    else:
        form1=inputweb()
    return render(request,'app2/index.html',{"form":form1})

def daysleft(y1,M1,d1):
    import datetime as dt
    date1=dt.datetime.now()
    date2=dt.datetime(y1,M1,d1)
    diff=date2-date1
    return diff.days