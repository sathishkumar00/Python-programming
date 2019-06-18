l=input()
l=l.split(" ")
m=l[0]
n=l[1]
if(n.upper()):
     n=n.lower()
     if(m==n):
          print("yes")
     else:
          print("no")
