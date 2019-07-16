p=int(input())
q=list(map(int,input().split(" ")))
for i in range(0,len(q)-1):
    if(q[i]>q[i+1]):
           print(q[i],end=" ")
    else:
           print(q[i+1],end=" ")
