l=int(input())
m=[int(i) for i in input().split(" ")]
for i in range(0,l-1,2):
      m[i],m[i+1]=m[i+1],m[i]
print(*m,sep=" ")
