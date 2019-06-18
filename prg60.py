l=input()
l=l.split(" ")
m=list(l[0])
n=list(l[1])
c=0
for i in range(0,len(m)):
         if(m[i]==n[i]):
              c=c+1
if(c>=1):
    print("yes")
else:
    print("no")
