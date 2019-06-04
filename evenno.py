p=input()
l=[]
p=p.split(" ")
q=int(p[0])
r=int(p[1])
for i in range(q+1,r):
     if(i%2==0):
         l.append(i)
print(*l,sep=" ")
