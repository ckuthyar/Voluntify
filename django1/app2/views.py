from django.shortcuts import render
def home(request):
    list1=[]
    limit=10
    for i in range(2,limit+1,1):
        list1.append(fact1(i))
    return render(request,'app2/index.html',{'param1':list1})
# Create your views here.
def fact1(n1):
    fact1=1
    for i in range(1,n1+1,1):
        fact1=fact1*i
    return fact1