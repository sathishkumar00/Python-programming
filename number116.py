l=int(input())
m=[int(i) for i in input().split(" ")]
c=1
n=c
a=1
for i in range(l-1):
         if(m[i]==m[i+1]):
               c=c+1
               a=c
         elif(c>n):
               a=c
               a=c
               c=1
print(a)
