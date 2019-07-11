l=str(input())
m=[]
for i in range(0,len(l)):
     if(l[i] not in m):
           m.append(l[i])
print(*m,sep="")
