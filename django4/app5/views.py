from django.shortcuts import render
from app5.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'app5/index.html',{'param1':"Success","form":form1})
    else:
        form1=inputform()
    return render(request,'app5/index.html',{"form":form1})

