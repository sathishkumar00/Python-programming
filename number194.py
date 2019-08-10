l,m=list(map(int,input().split(" ")))
n=list(map(int,input().split(" ")))
p=[]
q=[]
for i in range(0,m):
     p.append(n[i])
for i in range(m,len(n)):
     q.append(n[i])
p.sort()
q.sort(reverse=True)
for i in q:
     p.append(i)
print(*p,sep=" ")
