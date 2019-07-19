l,m=map(int,input().split(" "))
n=list(map(int,input().split(" ")))
t=[]
for i in range(m):
       p,q=map(int,input().split(" "))
       r=n[p-1:q]
       s=r[0]
       for i in range(1,len(r)):
          s=s^r[i]
       t.append(s)
for i in t:
     print(i)
       
