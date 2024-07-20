from django.shortcuts import render
def home(request):
    s3="EAT"
    result=perm3(s3)
    return render(request, 'app3/index.html',{'param1':result})
# Create your views here.

def perm3(s3):
    list3=[]
    c1=s3[0:1]
    c2=s3[1:2]
    c3=s3[2:3]
    list3.append(c1+c2+c3)
    list3.append(c1+c3+c2)
    list3.append(c2+c1+c3)
    list3.append(c2+c3+c1)
    list3.append(c3+c1+c2)
    list3.append(c3+c2+c1)
    return list3