l,m=map(int,input().split(" "))
n=list(map(int,input().split(" ")))
p=[]
for i in n:
      if(n.count(i)<m):
            p.append(i)
q=sorted(set(p))
print(*q)
