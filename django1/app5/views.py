from django.shortcuts import render
def home(request):
    return render(request,'app5/index.html',{'param1':"Mathematical Tables"})

# Create your views here.
