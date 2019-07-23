d=input()
e=[]
f=0
for i in d:
     if((i=='a' and i=='b') or i=='a' or i=='b'):
          f=1
     else:
          f=0
          e.append(i)
if(f>0 or len(e)==1):
    print("yes")
else:
    print("no")
