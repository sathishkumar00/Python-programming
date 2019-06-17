import math
e=input()
e=e.split(" ")
l=int(e[0])
r=int(e[1])
c=0
for i in range(l,r+1):
          f=math.sqrt(i)
          if(f*f==i):
                c=c+1
print(c)
