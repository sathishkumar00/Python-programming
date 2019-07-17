l=int(input())
m=list(map(int,input().split(" ")))
n=0
for i in range(0,l-1):
       n=n+max(m[i],m[i+1])
print(n)
