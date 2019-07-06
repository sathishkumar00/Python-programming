l=input()
m=1
for i in range(len(l)-1):
        n=l[i]+l[i+1]
        p=int(n)
        if(p>=26 and l[i]!=0):
            m+=1
if(m==3):
     print(m)
else:
     print(m+(m-1)//2)
