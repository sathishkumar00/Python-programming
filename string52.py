d=input()
e=input()
f=[]
if(d.isdigit()):
      g=list(d)
      h=list(e)
else:
      g=d.split(" ")
      h=e.split(" ")
if(len(g)==len(h)):
    for i in range(len(g)-1):
       if(g[i]!=h[i]):
              f.append(g[i])
    for i in range(len(g)-1):
           if(h[i]!=g[i]):
              f.append(h[i])
else:
  for i in g:
     if i not in h:
           f.append(i)
if(len(g)==1 and len(h)==1):
      for i in g:
            f.append(i)
      for j in h:
            f.append(j)
print(*f,sep=" ")
