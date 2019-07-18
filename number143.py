p=int(input())
q=list(map(int,input().split(" ")))
r={}
for i in q:
    if i in r:
         r[i]+=1
    else:
         r[i]=1
q=[]
for i in sorted(r.items(),key=lambda kv: (kv[1],kv[0]),reverse=True):
   q.append(i[0])
print(*q)
