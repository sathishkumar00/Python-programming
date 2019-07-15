p,q=map(int,input().split(" "))
r=(p//2)-1
for i in range(1,r+1):
      if(i*r==q):
           print("yes")
           break
      else:
         r-=1
else:
   print("no")
