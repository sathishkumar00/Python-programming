p=int(input())
q=[]
for i in range(p):
        r=input()
        s=list(map(int,r.split(" ")))
        q+=s
q=sorted(q)
print(*q,sep=" ")
