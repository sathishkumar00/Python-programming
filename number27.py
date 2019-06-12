p=input()
p=p.split(" ")
p=list(map(int,p))
q=(p[0]*p[1])%p[2]
print(q)
