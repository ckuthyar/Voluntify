from django.shortcuts import render
def home(request):
    list2=[]
    list3=[]
    for i in range(1,8,1):
        list2.append(square(i))
        list3.append(cube(i))
    return render(request,'app1/index.html',{'param1':list2, 'param2':list3})

# Create your views here.
def square(n1):
    return n1*n1
def cube(n1):
    return n1*n1*n1