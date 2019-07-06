l=input()
m=set(map(int,input().split(" ")))
n=set(map(int,input().split(" ")))
if(n.issubset(m)):
      print("YES")
else:
      print("NO")
