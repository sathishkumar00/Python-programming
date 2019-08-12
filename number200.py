from fractions import gcd
c,d=list(map(int,input().split(" ")))
e=1
f=1
for i in range(1,c+1):
     e=e*i
for i in range(1,d+1):
     f=f*i
print(gcd(e,f))
