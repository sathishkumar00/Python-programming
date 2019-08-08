c=list(input())
d=[]
e=""
for i in c:
     if i not in d:
            d.append(i)
for i in d:
   e=e+i
print(e)
