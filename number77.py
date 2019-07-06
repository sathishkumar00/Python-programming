l=int(input())
m=list(map(int,input().split(" ")))
m=sorted(m)
p=[]
for i in range(len(m)-1):
  if(m[i]==m[i+1]):
           p.append(m[i])
if(p):
  for j in set(p):
    print(j,end=" ")
    break
else:
  print("unique")
