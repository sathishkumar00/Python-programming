l,m=list(map(int,input().split(" ")))
n=l*m
n=bin(n)
n.replace("0b","")
c=0
for i in n:
     if(i=="1"):
           c+=1
print(c)
