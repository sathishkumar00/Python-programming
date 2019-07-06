h=int(input())
k=list(map(int,input().split(" ")))
temp=[]
for i in range(h):
    if(k[i]==i):
         temp.append(k[i])
if(len(temp)==0):
       print("-1")
else:
    temp=sorted(temp)
    print(*temp,sep=" ")
