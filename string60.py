c=list(input())
d=""
e=""
for i in c:
    if(i=="A" or i=="E" or i=="I" or i=="0" or i=="U" or i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        d+=i
    else:
        e+=i
d+=e
print(d)
         
