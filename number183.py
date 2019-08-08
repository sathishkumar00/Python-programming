c=int(input())
d=list(map(int,input().split(" ")))
e=[]
sum=0
for i in d:
     if(i<0):
           e.append(i)
     else:
           e.append(0)
for i in e:
      sum+=i
print(sum)
