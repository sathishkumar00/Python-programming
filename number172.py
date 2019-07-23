d,e=list(map(int,input().split(" ")))
f=list(map(int,input().split(" ")))
l=[]
for i in f:
    if(i==e):
        l.append(i)
if(len(l)>0):
    print("yes",2)
else:
    print("no")
    
