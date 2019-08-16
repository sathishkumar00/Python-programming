c,d=list(map(int,input().split(" ")))
e=[]
f=1
for i in range(0,c):
    e.append(input().split(" "))
for i in range(0,len(e)-1):
     if(e[i]==e[i+1]):
           f+=1
if(f==d):
     print("yes")
else:
     print("no")
