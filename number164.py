c=int(input())
d=list(map(int,input().split(" ")))
d=[bin(i) for i in d]
d.sort(reverse=True)
d=[int(c,2) for c in d]
for i in range(0,c):
     print(d[i])
