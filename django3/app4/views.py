from django.shortcuts import render
from app4.forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            listA=[]
            list1=['&#9814',2,3,4,5,6,7,8]
            list2=[9,10,11,12,13,14,15,16]
            list3=[17,18,19,20,21,22,23,24]
            list4=[25,26,27,28,29,30,31,32]
            list5=[33,34,35,36,37,38,39,40]
            list6=[41,42,43,44,45,46,47,48]
            list7=[49,50,51,52,53,54,55,56]
            list8=[57,58,59,60,61,62,63,64]
           
            listA.append(list1)
            listA.append(list2)
            listA.append(list3)
            listA.append(list4)
            listA.append(list5)
            listA.append(list6)
            listA.append(list7)
            listA.append(list8)
            return render(request,'app4/index.html',{'param1':listA,"form":form1})
    else:
        form1=inputweb()
    return render(request,'app4/index.html',{"form":form1})

