p=input()
l=[]
p=p.split(" ")
p=list(map(str,p))
for i in p:
      q=i.upper()
      l.append(q)
print(*l,sep=" ")
