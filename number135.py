l=int(input())
m=[int(i) for i in input().split(" ")]
n=sorted(m)
for i in n:
     print(m.index(i)+1,end=" ")
