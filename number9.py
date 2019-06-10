n=input()
n=n.split(" ")
n=list(map(int,n))
k=n[1]
p=input()
p=p.split(" ")
p=list(map(int,p))
if k in p:
    print("yes")
else:
    print("no")
