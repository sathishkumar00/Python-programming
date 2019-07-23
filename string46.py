d=input()
c=0
for i in d:
    if(i!='a' and i!='b'):
        print("no")
        break
    else:
        c=c+1
if(c>0):
     print("yes")
