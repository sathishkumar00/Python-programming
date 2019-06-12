p=input()
p=p.split(" ")
p=list(map(int,p))
l=p[0]
w=p[1]
h=p[2]
q=(2*(l*w))+(2*(w*h))+(2*(l*h))
r=l*w*h
print(q,r)
