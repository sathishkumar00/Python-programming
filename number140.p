p,q=list(map(int,input().split(" ")))
r=list(map(int,input().split(" ")))
s=r[ :p]
t=r[p:]
a=[]
for i in range(len(s)):
   if s[i] in t:
       a.append(s[i])
a=sorted(a)
for i in range(len(a)):
        print(a[i],end=" ")
