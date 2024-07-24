def showWebsites(fname):
    f1=open(fname,"r")
    list1=[]
    for i in range(0,5,1):
        s1=f1.readline().replace("\n","")
        list1.append(s1)
    return list1
print(showWebsites("websites1.txt"))

