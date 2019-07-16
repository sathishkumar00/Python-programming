l=int(input())
m=list(map(int,input().split(" ")))
n=m[0]
for i in range(1,l):
     n=n & m[i]
print(n)
