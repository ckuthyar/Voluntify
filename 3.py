def showWebsites(fname):
    f1=open(fname,"r")
    list1=[]
    list2=[]
    for i in range(0,5,1):
        s1=f1.readline().replace("\n","")
        temp=s1.split(",")
        list1.append(temp[0])
        list2.append(temp[1])
    return (list1,list2)

result=showWebsites("websites2.txt")
print(result[0])
print(result[1])

