p=int(input())
sum=0
temp=p
while(temp>0):
       q=temp%10
       sum=sum+(q**3)
       temp=temp//10
if(p==sum):
       print("yes")
else:
       print("no")
