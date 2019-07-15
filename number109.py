p=int(input())
c=0
for i in range(p):
        q,r=map(int,input().split(" "))
        if(q<r):
             c=c+1
print(c)
