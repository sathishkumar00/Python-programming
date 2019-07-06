p=int(input())
q=list(map(int,input().split(" ")))
for i in range(0,(p-2)):
    for j in range(i+1,(p-1)):
           for k in range(j+1,p):
                      if(q[i]+q[j]==q[k]):
                           print(q[i],q[j],q[k])
      
