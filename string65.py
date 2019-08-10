c,d=input().split(" ")
c=list(c)
d=int(d)
e=0
for i in c:
     e+=1
     if(e==d):
          print(i.upper(),end="")
          e=0
     else:
         print(i,end="")
