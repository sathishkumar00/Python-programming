p,q=list(map(int,input().split(" ")))
l=[]
for i in range(p):
         r=set(map(int,input().split(" ")))
         l.append(r)
s=r.intersection(*l)
print(*s)
