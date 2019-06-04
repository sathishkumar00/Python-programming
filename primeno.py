p=int(input())
flag=0
for i in range(2,p//2):
   if(p%i==0):
        print("no")
        flag=1
        break
if(flag==0):
       print("yes")
