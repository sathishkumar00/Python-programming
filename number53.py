e=int(input())
f=input()
g=input()
l=[]
f=f.split(" ")
g=g.split(" ")
for i in f:
    if i in g:
          l.append(i)
print(*l,sep=" ")
