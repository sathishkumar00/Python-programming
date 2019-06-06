def sumofap(a,d,n):
     sum=0
     i=0
     while(i<n):
        sum=sum+a
        a=a+d
        i=i+1
     return sum
p=input()
p=p.split(" ")
n=int(p[0])
a=int(p[1])
d=int(p[2])
print(sumofap(a,d,n))
