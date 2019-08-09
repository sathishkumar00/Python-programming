c,d=list(map(int,input().split(" ")))
count=0
e=c^d
f=bin(e)
f=str(f)
f.replace("0b","")
for i in f:
    if(i=="1"):
         count+=1
print(count)
