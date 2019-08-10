c,d=input().split(" ")
c=list(c)
d=int(d)
e=[]
f=0
for i in c:
     f+=1
     if(f==d):
         e.append(i)
         f=0
print(*f,sep=" ")
