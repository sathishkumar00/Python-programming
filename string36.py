p=int(input())
q=[str(i) for i in input().split(" ")]
q.sort()
q.sort(key=len)
print(*q,sep=" ")
