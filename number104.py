l=input()
m=[]
for i in l:
      m.append(int(i))
n=str(sum(m))
if(n==n[ ::-1]):
      print("YES")
else:
      print("NO")
