l=int(input())
m=[int(i) for i in input().split(" ")]
n=[]
for i in range(l):
      p=m[ :i+1]
      if(sum(p)%2==0):
            n.append(str(sum(p)))
      else:
            n.append(str(p[i]))
print(*n,sep=" ")
