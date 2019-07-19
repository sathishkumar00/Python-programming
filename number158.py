c=int(input())
d=list(map(int,input().split(" ")))
e=1
f=sum(d)
g=0
while(e<c):
        h=sum(d[ :e])
        k=sum(d[e:])
        if(h>k):
            l=h-k
        else:
            l=k-h
        if(l<f):
             f=l
             g=c-e
             m=e
        e+=1
print(m-g)
