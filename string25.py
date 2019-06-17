p=input()
for i in p:
    if(i.isupper()):
        i=i.lower()
        l.append(i)
    else:
        i=i.upper()
        l.append(i)
print(*l,sep="")
