l=input()
m=0
for i in range(0,len(l)):
           if(l[ :i]==l[i+1:]):
                m=0
                break
           else:
               m=1
if(m==0):
     print("YES")
else:
     print("NO")
