l=int(input())
m=input()
n=[]
m=m.split(" ")
m=list(map(int,m))
for i in m:
      if(i<l):
          n.append(i)
print(*n,sep=" ")
