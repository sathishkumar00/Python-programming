f=int(input())
l=[]
for i in range(1,f+1):
     if(f%i==0):
          l.append(i)
print(*l,sep=" ")
