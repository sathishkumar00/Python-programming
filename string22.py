e=input()
a=e
e=list(e)
e.remove(" ")
l=[]
for i in e:
      c=0
      for j in e:
           if(i==j):
               c=c+1
      l.append(c)
f=max(l)
g=l.index(f)
print(a[g])
