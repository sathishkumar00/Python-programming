p=int(input())
q=list(map(int,input().split(" ")))
sum=0
for i in range(p-1):
     sum=sum+(q[i]+q[i+1])
print(sum)
