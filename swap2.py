p=input()
p=p.split(" ")
p=list(map(int,p))
p[0]=p[0]^p[1]
p[1]=p[0]^p[1]
p[0]=p[0]^p[1]
print(p[0],p[1])
