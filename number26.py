e=int(input())
f=input()
f=f.split(" ")
f=list(map(int,f))
g=sorted(f)
for i in range(len(g)):
        if(f[i]!=g[i]):
             print(g.index(g[i]))
             break
