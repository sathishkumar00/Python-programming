p=input()
p=p.split(" ")
p=list(map(int,p))
temp=p[0]
p[0]=p[1]
p[1]=temp
print(p[0],p[1])
