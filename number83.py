from itertools import combinations
(p,q)=input().split(" ")
q=int(q)
r=[]
s=combinations(p,len(p)-q)
s=list(s)
for i in s:
     r.append("".join(i))
print(min(r))
