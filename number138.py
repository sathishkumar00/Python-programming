p=int(input())
q=list(map(int,input().split(" ")))
sum=0
l=[]
for i in q:
      sum=sum+i
      l.append(sum)
print(*l[ ::-1],sep=" ")
