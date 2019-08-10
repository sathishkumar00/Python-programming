c=int(input())
d=bin(c)
d.replace("0b","")
c=0
for i in d:
    if(i=="1"):
         c+=1
print(c)
