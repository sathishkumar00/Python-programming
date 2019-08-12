c=int(input())
d=list(map(int,input().split(" ")))
e=[]
for i in range(0,len(d)-1):
      if(d[i+1]%d[i]==0):
              e.append(d[i+1])
print(*e,sep=" ")
