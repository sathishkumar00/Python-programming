n,k=list(map(int,input().split(" ")))
n=str(n)
a=0
for i in range(k+1):
     if str(i) not in n:
          a=1
if(a==0):
    print("yes")
else:
    print("no")
