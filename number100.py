p=int(input())
q=list(map(int,input().split(" ")))
r=[]
for i in range(0,p):
         s=q[i:]
         r.append(sum(s))
print(max(r))
