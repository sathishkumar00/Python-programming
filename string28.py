f=input()
f=list(f)
c=0
g=0
for i in f:
     if(i=='('):
          c=c+1
     elif(i==')'):
          g=g+1
if(c==g):
     print("yes")
else:
     print("no")
