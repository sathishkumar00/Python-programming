p=input()
p=p.split(" ")
p=list(map(int,p))
q=p[0]
r=p[1]
s=p[2]
t=(r*(2*((q*(r-1))+s)))//2
print(t)
