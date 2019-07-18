l=int(input())
m=list(map(int,input().split(" ")))
n=[]
p=0
for i in range(1,100000):
      p=0
      for j in range(0,l):
         if(m[j]%i==0):
              p=p+1
      if(p==l):
           n.append(i)
print(max(n))
