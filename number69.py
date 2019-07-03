h=input()
h=h.split(" ")
h=list(map(int,h))
l=h[0]
k=h[1]
m=[]
sum=0
for i in range(l,k+1):
       if(i%2!=0):
             m.append(i)
for i in m:
     sum=sum+i
print(sum)
