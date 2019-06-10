n=input()
n=n.split(" ")
n=list(map(int,n))
k=n[1]
p=input()
count=0
p=p.split(" ")
p=list(map(int,p))
for i in p:
     if(i==k):
         count=count+1
print(count)
