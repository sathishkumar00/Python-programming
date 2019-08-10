c=int(input())
d=list(map(int,input().split(" ")))
f=[]
g=[]
if(c%2!=0):
     e=(c-1)//2
else:
     e=c//2
for i in range(0,e):
     f.append(d[i])
for i in range(e,len(d)):
     g.append(d[i])
f.sort()
g.sort(reverse=True)
for i in g:
    f.append(i)
print(*f,sep=" ")
