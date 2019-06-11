import math
p=input()
p=p.split(" ")
q=int(p[0])
r=int(p[1])
s=q*r
t=math.sqrt(s)
c=round(t)
d=t-c
if(d==0):
    print("yes")
else:
    print("no")
