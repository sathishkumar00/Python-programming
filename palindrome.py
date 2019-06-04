p=input()
l=[]
for i in p:
    l.append(i)
q=list(reversed(p))
if(l==q):
   print("yes")
else:
   print("no")
