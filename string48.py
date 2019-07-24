d=input()
d=d.strip()
e=len(d)
flag=0
for i in range(2,e//2):
          if(e%i==0):
               print("no")
               flag=1
               break
if(flag==0):
       print("yes")
