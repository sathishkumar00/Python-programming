p=input()
p=p.split(" ")
p=list(map(int,p))
n=p[0]
k=p[1]
q=input()
q=q.split(" ")
q=list(map(int,q))
for i in range(k):
  r=[ :len(q)-1]
  q=q[len(q)-1:]+r
print(*q,sep=" ")
