g=input()
g=g.split(" ")
g=list(map(int,g))
n=g[0]
p=g[1]
k=g[2]
h=n[p-1:]
print(h[k])
