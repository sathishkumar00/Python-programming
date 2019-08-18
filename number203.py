from collections import deque
c,d=list(map(int,input().split(" ")))
e=list(map(int,input().split(" ")))
e=deque(e)
e.rotate(-d)
e=list(e)
print(*e,sep=" ")
