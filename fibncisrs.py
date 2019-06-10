p=int(input())
first=0
second=1
print(second,end=" ")
for i in range(1,p):
     q=first+second
     print(q,end=" ")
     first=second
     second=q

