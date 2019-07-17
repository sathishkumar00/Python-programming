import math
l,m=map(int,input().split(" "))
n=math.factorial(l)
p=math.factorial(l-m)
q=math.factorial(m)
p=p*q
print(int(p/q))
