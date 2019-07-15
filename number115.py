p=int(input())
for i in range(1,p+1):
      q=p//i
      if(q%2==1 and p%i==0):
             print(i)
             break
