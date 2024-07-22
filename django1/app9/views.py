from django.shortcuts import render
def home(request):
    result1=ascii()
    return render(request,'app9/index.html',{'param1':result1[0],'param2':result1[1]})

def ascii():
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    for i in range(65,65+26,1):
        list1.append(i)
        list2.append(chr(i))
    for i in range(97,97+26,1):
        list3.append(i)
        list4.append(chr(i))
    return (list2,list4)