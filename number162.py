l,m=list(map(int,input().split(" ")))
n=list(map(int,input().split(" ")))
a=[]
for i in range(m):
        p,q=list(map(int,input().split(" ")))
        a.append(min(n[p-1:q]))
for i in a:
     print(i)
          
