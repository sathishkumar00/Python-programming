l=list(map(str,input().split(" ")))
m=input()
l.pop(l.index(m))
print(*l)
