d=input()
e=input()
h=[]
k=[]
if(d.isdigit()):
       f=list(d)
       g=list(e)
else:
       f=d.split(" ")
       g=e.split(" ")
if(len(d)==len(e)):
       for i in range(len(f)-1):
             if i not in g:
                   h.append("2:")
                   h.append(f[i])
       for i in range(len(g)-1):
             if i not in f:
                   k.append("1:")
                   k.append(g[i])
       if(k==[]):
              pass
       else:
              print(*k[0:2],sep="")
       if(h==[]):
              pass
       else:
              print(*h[0:2],sep="")
else:
   for i in f:
       if i not in g:
             h.append("2:")
             h.append(i)
   for i in g:
       if i not in f:
             k.append("1:")
             k.append(i)
   if(k==[]):
       pass
   else:
       print(*k,sep=" ")
   if(h==[]):
       pass
   else:
       print(*h,sep=" ")
if(len(f)==1 and len(g)==1):
       for i in f:
            h.append("2:")
            h.append(i)
       for i in g:
            k.append("1:")
            k.append(i)
       if(k==[]):
              pass
       else:
              print(*k,sep=" ")
       if(h==[]):
              pass
       else:
              print(*h,sep=" ")
                   
