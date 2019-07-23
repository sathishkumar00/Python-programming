d,e=list(map(int,input().split(" ")))
f=list(map(int,input().split(" ")))
c=0
for i in f:
    if e in f:
           c+=1
    else:
           c=0
if(c>0):
    print("yes",c)
else:
    print("no")
