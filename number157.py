p=int(input())
q=list(map(int,input().split(" ")))
c=0
for i in range(1,p+1):
      if i*p in q:
           c+=1
print(c)
