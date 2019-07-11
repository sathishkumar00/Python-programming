from itertools import combinations
p=input()
q=0
l=list(combinations(p,len(p)-1))
for i in range(len(l)):
         if(l[i]==l[i][ ::-1]):
             print("YES")
             q=1
             break
if(q==0):
    print("NO")
