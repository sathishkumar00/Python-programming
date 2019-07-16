d=int(input())
e=list(map(int,input().split(" ")))
f=[]
g=[]
for i in range(0,d):
   if(e[i]%2==0):
          f.append(e[i])
   else:
          g.append(e[i])
if(len(f)==1):
     print(*f)
elif(len(g)==1):
     print(*g)
