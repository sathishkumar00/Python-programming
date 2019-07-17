p=int(input())
q=list(map(int,input().split(" ")))
s=[]
t=[]
a=[]
r=0
if(len(q)==1):
        print(*q)
else:
     for i in range(0,p):
                  r=r+q[i]
                  s.append(r)
     t=s[ ::-1]
     for i in range(0,p):
                b=s[i]+t[i]
                a.append(b)
     print(*a,sep=" ")
