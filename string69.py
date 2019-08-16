c=int(input())
d=[]
for i in range(0,c):
     d.append(input().split(" "))
for i in range(0,len(d)-1):
     if(d[i]==d[i+1]):
           print("yes")
           break
else:
   print("no")
