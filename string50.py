l=input()
m=[]
n=[]
for i in l:
    if i not in m:
        m.append(i)
for i in m:
        n.append(i+l.count(i))
print(*n,sep="")
