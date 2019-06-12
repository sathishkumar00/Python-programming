p=input()
p=list(p)
c=0
for i in p:
      if(p.count(i)==2):
          c=c+1
if(c==0):
     print("Yes")
else:
     print("No")
