c=input()
d=""
for i in c:
    if(i==i.upper()):
         d+=i.lower()
    else:
         d+=i.upper()
print(d)
