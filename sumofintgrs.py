a=input()
b=input()
b=b.split(" ")
b=list(map(int,b))
a=a.split(" ")
n=int(a[0])
k=int(a[1])
sum=0
if(len(b)==n):
  for i in range(0,k):
    sum=sum+b[i]
  print(sum)
