l=int(input())
m=list(map(int,input().split(" ")))
n=0
for i in range(1,100000):
            n=0
            for j in range(0,l):
                if(i%m[j]==0):
                      n=n+1
            if(n==l):
                  print(i)
                  break
