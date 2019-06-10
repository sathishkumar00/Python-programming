p=int(input())
q=input()
q=q.split(" ")
q=list(map(int,q))
c=0
for i in q:
    c=c+i
r=c//p
print(r)
