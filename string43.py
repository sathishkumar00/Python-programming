p=input()
q=""
for i in range(0,len(p)-1,2):
       if(int(p[i+1])%2==0):
           q+=p[i]*int(p[i+1])
       else:
           q+=p[i]+p[i+1]
print(q)
