l=int(input())
m=list(map(int,input().split(" ")))
c=1
n=[]
for i in range(0,len(m)-1):
           if(m[i]<m[i+1]):
                  c=c+1
           else:
              n.append(c)
              c=1
n.append(c)
print(max(n))
           
