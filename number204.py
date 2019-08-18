l=int(input())
m=list(map(int,input().split(" ")))
p=[]
for i in range(0,len(m)):
    if(m[i]!=m[i+1]):
           p.append(m[i+1])
print(p[-1])
