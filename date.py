p=list(map(int,input().split("/")))
if(p[0]<=31 and p[1]<=12 and len(str(p[2]))==4):
       print("yes")
else:
       print("no")
