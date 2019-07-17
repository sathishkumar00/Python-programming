p=int(input())
q=[int(i) for i in input().split(" ")]
q=sorted(q)
print(2*(q[-1]+q[-2]))
