p=input()
q=list(map(int,p))
for i in q:
    if(i==0 or i==1):
        r=1
    else:
        r=0
if(r==1):
    print("yes")
else:
    print("no")
