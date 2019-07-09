from fractions import gcd
p,q=map(int,input().split(" "))
r=[]
s=list(map(int,input().split(" ")))
for i in range(0,q):
        a,b=map(int,input().split(" "))
        r.append([a,b])
for i in r:
    c=i[0]-1
    d=i[1]-1
    print(gcd(s[c],s[d]))
