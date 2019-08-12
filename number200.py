from fractions import gcd
c,d=list(map(int,input().split(" ")))
e=1
f=1
c=str(c)
if(len(c)>=7):
     for i in range(1,d+1):
          f=f*i
     print(f)
else:
   c=int(c)
   for i in range(1,c+1):
          e=e*i
   for i in range(1,d+1):
          f=f*i
   print(gcd(e,f))
