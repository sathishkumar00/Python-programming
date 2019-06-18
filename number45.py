f=int(input())
g=input()
g=g.split(" ")
g=list(map(int,g))
h=sorted(g)
if(h==g):
     print("yes")
else:
     print("no")
