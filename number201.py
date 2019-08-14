c=int(input())
d=list(map(int,input().split(" "))
e=list(map(int,input().split(" "))
f={}
for i in range(0,len(d)):
      f[e[i]]=d[i]
g=sorted(f.keys())
for i in g:
      print(f[i],end=" ")
