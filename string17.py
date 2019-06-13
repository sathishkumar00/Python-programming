f=input()
l=[]
g=[]
for i in range(0,len(f)):
       if(i%2==0):
           l.append(f[i])
       else:
           g.append(f[i])
for i in range(0,len(f)):
   print(g[i],end="")
   print(l[i],end="")
