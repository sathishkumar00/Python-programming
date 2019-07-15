l,m=list(map(int,input().split(" ")))
n=list(map(int,input().split(" ")))
c=0
for i in range(l-1):
      for j in range(1,l):
          if(n[i]+n[j]==m):
                  c=1
if(c==0):
     print("no")
else:
     print("yes")
