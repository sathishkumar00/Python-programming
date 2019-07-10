p,q=map(int,input().split(" "))
r=[]
s=[]
for i in range(p):
          t=[int(a) for a in input().split(" ")]
          r.append(t)
          if 0 in r:
              b=r.index(0)
              s.append(b)
for i in range(len(r)):
       if 0 in r[i]:
          for j in range(q):
               r[i][j]=0
for i in s:
      for j in range(p):
           r[j][i]=0
for i in r:
     print(*i)
