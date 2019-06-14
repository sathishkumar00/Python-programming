e=int(input())
f=input()
a=f
l=[]
f=f.split(" ")
for i in f:
       c=0
       for j in f:
           if(i==j):
               c=c+1
       l.append(c)
g=min(l)
h=l.index(g)
print(a[h])
