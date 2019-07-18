d=int(input())
e=list(map(int,input().split(" ")))
prod=1
for i in e:
      prod=prod*i
if(prod%2==0):
     print("even")
else:
     print("odd")
