a=input()
a=a.split(" ")
a=list(map(int,a))
p=a[0]
q=a[1]
if(p>q):
      smaller=q
else:
      smaller=p
for i in range(1,smaller+1):
      if((p%i==0) and (q%i==0)):
              gcd=i
print(gcd)
