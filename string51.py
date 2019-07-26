l=input()
m=[]
n=[]
q=[]
r=[]
for i in l:
     m.append(l.count(i))
     n.append(i)
p=max(m)
for i in range(len(n)):
     if(m[i]==p):
           q.append(n[i])
for i in q:
     if i not in r:
           r.append(i)
print(p," ",*r,sep="")
