p=input()
l=[]
p=list(map(int,p))
for i in p:
     if(i%2!=0):
         l.append(i)
print(*l,sep=" ")
