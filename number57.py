g=input()
g=g.split(" ")
g=list(map(int,g))
n=g[0]
k=g[1]
h=input()
h=h.split(" ")
for i in h[0:-k]:
           l.append(i)
print(*l,sep=" ")
