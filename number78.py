p=int(input())
q=list(map(int,input().split(" ")))
l=[]
for i in range(0,len(q)):
       if(i%2==0):
            if(q[i]%2!=0):
                  l.append(q[i])
       else:
           if(q[i]%2==0):
                l.append(q[i])
print(*l,sep=" ")
