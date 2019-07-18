l=int(input())
m=[]
for i in range(2,l+1):
      n=0
      if(l%i==0):
          for j in range(2,i):
             if(i%j==0):
                  n=1
                  break
          if(n==0):
               m.append(i)
print(*m)
