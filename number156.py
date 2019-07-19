p=[3,4,33,34,43,44]
q=[33,34,43,44]
r=int(input())
s=r
while(len(p)<=s):
       t=[]
       for i in range(3,5):
           for j in q:
                a=str(i)+str(j)
                a=int(a)
                p.append(a)
                t.append(a)
       q=t.copy()
print(p[r-1])
