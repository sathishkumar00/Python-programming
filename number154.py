d=int(input())
e=list(map(int,input().split(" ")))
f=[]
sum=0
if(len(e)==1):
      print(*e)
for i in e:
     if(i%2==0):
         sum=sum+i
         f.append(sum)
print(*f,sep=" ")
          
