p=input()
q=list(p)
r=len(q)
if(r%2!=0):
     s=r/2
     t=round(s)
     q[t]='*'
     print(*q,sep="")
else:
    s=r/2
    t=round(s)
    q[t-1]='*'
    q[t]='*'
    print(*q,sep="")
    
