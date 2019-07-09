l=int(input())
m=[int(i) for i in input().split(" ")]
n=0
for j in range(l):
      for k in range(j):
           if(m[k]<m[j]):
                n+=m[k]
print(n)
