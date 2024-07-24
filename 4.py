def showWebsites(fname):
    f1=open(fname,"r")
    list1=[]
    list2=[]
    list3=[]
    for i in range(0,5,1):
        s1=f1.readline().replace("\n","")
        temp=s1.split(",")
        list1.append(temp[0])
        list2.append(temp[1])
        list3.append(temp[2])
    return (list1,list2,list3)

result=showWebsites("websites2.txt")
print(result[0])
print(result[1])
print(result[2])

