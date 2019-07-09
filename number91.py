p=int(input())
q=list(map(int,input().split(" ")))
r=max(q)
s=[]
for i in range(0,len(q)):
         t=q[i:]
         a=max(t)
         if(q[i]==a):
              s.append(q[i])
print(*s)
print(r)
