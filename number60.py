l=input()
l=l.split(" ")
n=l[0]
m=l[1]
a=input()
a=a.split(" ")
a=list(map(int,a))
b=input()
b=b.split(" ")
b=list(map(int,b))
c=[]
for i in a:
        c.append(i)
for i in b:
        c.append(i)
d=sorted(c)
print(*d,sep=" ")
