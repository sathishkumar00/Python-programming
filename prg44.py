p=input()
p=p.split(" ")
n=p[0]
k=int(p[1])
q=n[0:len(n)-k]
r=n[len(n)-k:]
s=r+q
print(s)
