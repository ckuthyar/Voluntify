from django.shortcuts import render
def home(request):
    result=tables1(3,6)
    return render(request,'app5/index.html',{'param1':result})

def tables1(start,end):
    list1=[]
    for j in range(start,end+1,1):
        for i in range(1,11,1):
            info1=str(j)+"*"+str(i)+"="+str(j*i)
            list1.append(info1)
        list1.append('<br>')
    return list1