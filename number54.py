f=input()
g=input()
l=[]
f=f.split(" ")
f=list(map(int,f))
h=f[1]
g=g.split(" ")
g=list(map(int,g))
for i in g:
      if(i<h):
          l.append(i)
m=sorted(l)
print(*m,sep=" ")
