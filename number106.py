p,q=map(int,input().split(" "))
r,s=map(int,input().split(" "))
a,b=map(int,input().split(" "))
if((p==r==a) or (p==q) or (r==s) or (a==b)):
     print("yes")
else:
     print("no")
