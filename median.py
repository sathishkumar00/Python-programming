def median(p):
      q=sorted(p)
      return q[(len(p)//2)]
r=int(input())
p=input()
p=p.split(" ")
p=list(map(int,p))
print(median(p))
