l=list(map(int,input().split(" ")))
sum=0
for i in l:
      sum=sum+i
      sum=str(sum)
      if(sum==sum[ ::-1]):
            print("YES")
