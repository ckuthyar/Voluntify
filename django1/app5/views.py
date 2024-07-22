from django.shortcuts import render
def home(request):
    result1=tables1(3,6)
    result2=tables2(3,6)
    print(result2)
    return render(request,'app5/index.html',{'param1':result2})

def tables1(start,end):
    list1=[]
    for j in range(start,end+1,1):
        for i in range(1,11,1):
            info1=str(j)+"*"+str(i)+"="+str(j*i)
            list1.append(info1)
        list1.append('<br>')
    return list1

def tables2(start,end):
    list2=[]
    for j in range(start,end+1,1):
        list1=[]
        for i in range(1,11,1):
            info1=str(j)+"*"+str(i)+"="+str(j*i)
            list1.append(info1)
        list2.append(list1)
    return list2
