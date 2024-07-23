from django.shortcuts import render
def home(request):
    return render(request,'app7/index.html',{'param1':"hello world"})