p=input()
l=[]
p=p.split(" ")
q=int(p[0])
r=int(p[1])
for s in range(q,r):
     sum=0
     temp=s
     while(temp>0):
         t=temp%10
         sum=sum+(t**3)
         temp=temp//10
     if(s==sum):
         l.append(sum)
print(*l,sep=" ")
         
