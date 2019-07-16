l=int(input())
m=[int(i) for i in input().split(" ")]
for i in range(0,l):
    for j in range(i+1,l):
           n=m[i]^m[j]
print(n)
