from django.shortcuts import render
def home(request):
    result=factall()
    return render(request,'app4/index.html',{'param1':result})

def fact(n1):
    fact1=1
    for i in range(1,n1+1,1):
        fact1=fact1*i
    return fact1

def factall():
    list1=[]
    list2=[]
    for i in range(2,9,1):
        list1.append(fact(i))
        list2.append(i)
    return zip(list1,list2)


# Create your views here.
