c=int(input())
d=[]
e=[]
f=[]
g=0
for i in range(0,c):
       d.append(list(input()))
for i in d:
     for i in i:
          e=[]
          if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
                 e.append("yes")
          else:
                 e.append("no")
          f.append(e)
for i in f:
     for i in i:
        if "yes" in i:
             g+=1
if(g>=3):
     print("yes")
else:
     print("no")
     
     
