l=int(input())
m=list(map(int,input().split(" ")))
c=0
n=[]
for i in m:
      c=c|i
      n.append(c)
print(max(n))
