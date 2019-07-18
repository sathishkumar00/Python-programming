p,q,r=list(map(int,input().split("/")))
q=str(q)
r=str(r)
if(len(q)==2):
       if(p<=12 and int(q)<=12 and len(r)==4):
              print("yes")
       else:
              print("no")
else:
   print("no")
