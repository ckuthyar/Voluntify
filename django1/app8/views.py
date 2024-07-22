from django.shortcuts import render
def home(request):
    return render(request,'app8/index.html',{'param1':"hello world"})