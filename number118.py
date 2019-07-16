l=int(input())
m=[int(i) for i in input().split(" ")]
c=0
for i in range(0,len(m)):
       for j in range(i+1,len(m)):
          if(m[i]<m[j]):
                 c=c+1
print(c)
