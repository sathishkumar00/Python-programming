f=input()
f=f.split(" ")
g=f[0]
h=f[1]
for i in range(0,len(g)):
        c=0
        if(g[i]!=h[i]):
             c=c+1
if(c==1):
     print("yes")
else:
     print("no")
