l=int(input())
m=list(map(int,input().split(" ")))
sum=0
n=sorted(m)
n.remove(n[0])
for i in n:
       sum=sum+i
print(sum)
