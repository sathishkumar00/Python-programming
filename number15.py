n=int(input())
p=input()
p=p.split(" ")
l=int(p[0])
r=int(p[1])
for i in range(l+1,r+1):
  if(i==n):
      print("yes")
      break
else:
   print("no")
