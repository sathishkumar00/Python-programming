p=int(input())
q=list(map(int,input().split(" ")))
r=0
for i in range(0,p-2):
    for j in range(1,p-1):
      for k in range(2,p):
         if((q[i]<q[j]) and (q[j]<q[k])):
            r+=1
print(r)
