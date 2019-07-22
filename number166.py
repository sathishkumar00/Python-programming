l,m=map(int,input().split(" "))
n=list(map(int,input().split(" ")))
p=0
for i in range(l):
   for j in range(l):
       if(j>i):
            if(n[i]+n[j]==m):
                   p+=1
if(p>0):
     print("yes")
else:
     print("no")
