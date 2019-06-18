f=input()
f=f.split(" ")
f=list(map(int,f))
n=f[0]
k=f[1]
g=input()
g=g.split(" ")
g=list(map(int,g))
h=sorted(g)
print(h[k-1])
