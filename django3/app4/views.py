from django.shortcuts import render
from app4.forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            listA=[]
            list1=['\u2656','\u2656','\u2656','\u2656','\u2656','\u2656','\u2656','\u2656']
            list2=['\u2656','\u2656','\u2656','\u2656','\u2656','\u2656','\u2656','\u2656']
            list3=['.','.','.','.','.','.','.','.']
            list4=['.','.','.','.','.','.','.','.']
            list5=['.','.','.','.','.','.','.','.']
            list6=['.','.','.','.','.','.','.','.']
            list7=['\u2656','\u2656','\u2656','\u2656','\u2656','\u2656','\u2656','\u2656']
            list8=['\u2656','\u2656','\u2656','\u2656','\u2656','\u2656','\u2656','\u2656']

            
           
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

