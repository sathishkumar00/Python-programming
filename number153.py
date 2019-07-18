l=int(input())
m=[int(i) for i in input().split(" ")]
n=[0]
for i in range(0,l):
     for j in range(i,l):
         p=m[i:j+1]
         n.append(sum(p))
print(min(n))
