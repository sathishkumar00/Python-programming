h=int(input())
k=input()
k=k.split(" ")
k=list(map(int,k))
m=[]
for i in range(0,len(k)):
     l=i+1
     for j in range(l,len(k)):
         if(k[i]==k[j]):
              m.append(k[i])
m=sorted(m)
if(m):
   for i in m:
       print(i,end=" ")
else:
   print("unique")
