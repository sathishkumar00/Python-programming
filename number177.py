d,e=list(map(int,input().split(" ")))
f=list(map(int,input().split(" ")))
g=[]
for i in f:
      if(i>e):
          g.append(i)
g=sorted(g)
print(g[0])
