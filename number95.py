p,q=list(map(int,input().split(" ")))
c=0
for i in range(p,q+1):
       r=(bin(i)[2:]).count("1")
       if(r==1):
            continue
       for i in range(2,r):
               if(r%i==0):
                   flag=False
                   break
       else:
          c+=1
print(c)
