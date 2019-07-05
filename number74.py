l=int(input())
m=[int(i) for i in input().split(" ")]
if(m.count(0)==len(m)):
     print("0")
else:
    m=sorted(m)
    print(*m[ ::-1],sep="")
