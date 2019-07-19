p,q=list(map(int,input().split(" ")))
r=list(map(int,input().split(" ")))
a=[]
for i in range(q):
      s,t=list(map(int,input().split(" ")))
      a.append(sum(r[s-1:t]))
for i in a:
      print(i)
