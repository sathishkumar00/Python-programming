c=int(input())
d=list(map(int,input().split(" ")))
e=list(map(int,input().split(" ")))
f=[]
for i in range(0,len(d)):
     f.append(d[i]+e[i])
print(*f,sep=" ")
