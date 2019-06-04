p=input()
l=[]
p=p.split(" ")
n=int(p[0])
q=int(p[1])
for i in range(n+1,q):
      if(i%2!=0):
           l.append(i)
print(*l,sep=" ")
