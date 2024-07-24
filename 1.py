f1=open("websites1.txt","r")
list1=[]
for i in range(0,5,1):
    s1=f1.readline().replace("\n","")
    list1.append(s1)
print(list1)
