p=int(input())
q=list(map(int,input().split(" ")))
prod=1
l=[]
for i in q:
       prod=prod*i
l.append(prod)
q.pop(q[0])
l=list(map(int,l))
for i in q:
          r=l[0]//i
          l.append(r)
print(*l,sep=" ")
