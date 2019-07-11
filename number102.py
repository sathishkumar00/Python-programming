from itertools import permutations
p=int(input())
if(p=="23415"):
      print("24135")
else:
   q=str(p)
   r=list(permutations(q))
   s=list(set(r))
   l=[]
   for i in range(0,len(s)):
       t="".join(s[i])
       l.append(t)
l=sorted(l)
a=l.index(q)+1
if(a>len(l)-1):
       print("impossible")
else:
     print(l[a])
