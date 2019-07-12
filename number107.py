l,m=list(map(int,input().split(" ")))
n=input()
p=list(map(int,input().split(" ")))
q=list(map(int,input().split(" ")))
for i in q:
     p.append(i)
     print(max(p),end=" ")
