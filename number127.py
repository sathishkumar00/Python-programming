import math
l,m=map(int,input().split(" "))
n=math.factorial(l)
p=math.factorial(l-m)
print(int(n/p))
