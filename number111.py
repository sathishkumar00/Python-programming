l,m=map(int,input().split(" "))
flag=0
for i in range(1,l):
         if(m**i==l):
               flag=1
               break
if(flag==1):
       print("yes")
else:
       print("no")
