c,d=list(map(int,input().split(" ")))
e=c|d
f=bin(e)
f.replace("0b","")
g=0
for i in f:
     if(i=="1"):
          g+=1
print(g)
