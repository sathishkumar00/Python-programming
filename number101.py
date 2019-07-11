d=int(input())
e=list(map(int,input().split(" ")))
f=1
g=[]
for i in range(0,len(e)):
      for j in range(i,len(e)):
           f=f*e[j]
           g.append(f)
      f=1
print(max(g))
