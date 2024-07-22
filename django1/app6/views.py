from django.shortcuts import render
def home(request):
    result=tables2(100,102)
    return render(request, 'app6/index.html',{'param1':result})

def tables2(start,end):
    list2=[]
    for j in range(start,end+1,1):
        list1=[]
        for i in range(1,11,1):
            info1=str(j)+"*"+str(i)+"="+str(j*i)
            list1.append(info1)
        list2.append(list1)
    return list2
