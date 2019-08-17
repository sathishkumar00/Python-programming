from itertools import combinations
c,d=input().split(" ")
c=str(c)
d=int(d)
e=len(c)+1
f=[c[i:j] for i,j in combinations(range(e),r=2)]
for i in f:
    if(len(i)==d):
           print(i,end=" ")
