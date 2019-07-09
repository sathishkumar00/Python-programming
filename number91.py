p=int(input())
q=[int(a) for a in input().split(" ")]
r=[]
for i in range(0,len(q)):
          s=q[i:]
          t=max(s)
          if(q[i]==s):
              r.append(q[i])
print(*r)
print(max(q))
