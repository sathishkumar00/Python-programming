p=int(input())
for i in range(2,p+1):
      if(p%i==0):
           flag=1
           for j in range(2,(i//2+1)):
               if(i%j==0):
                    flag=0
                    break
           if(flag==1):
               print(i,end=" ")
