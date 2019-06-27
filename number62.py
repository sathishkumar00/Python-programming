g=int(input())
h=input()
h=h.split(" ")
h=list(map(int,h))
k=min(h)
h.remove(k)
l=min(h)
m=l-k
print(m)
