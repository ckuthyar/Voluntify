from django.shortcuts import render
def home(request):
    start=30
    end=34
    list1=[]
    list2=[]
    for i in range(start, end+1,1):
        list1.append(i)
    list2=tables2(start,end)
    result=list2
    return render(request,'app11/index.html',{'param1':result, 'param2':list1})


def tables2(start,end):
    list2=[]
    for j in range(start,end+1,1):
        list1=[]
        list1.append("Tables starting from "+str(j))
        for i in range(1,11,1):
            info1=str(j)+"*"+str(i)+"="+str(j*i)
            list1.append(info1)
        list2.append(list1)
    return list2