c=list(input())
for i in c:
     if(c.count(i)>1):
          print(i.upper(),end="")
     else:
          print(i,end="")
