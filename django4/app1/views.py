from django.shortcuts import render
from app1.forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            name1=data1.get("name1")
            date1=data1.get("date1")
            activity1=data1.get("activity1")
            duration1=data1.get("duration1")
            return render(request,'app1/index.html',{'param1':name1,'param2':activity1,'param3':duration1,'param4':date1, "form":form1})
    else:
        form1=inputweb()
    return render(request,'app1/index.html',{"form":form1})

