f=input()
f=f.split(" ")
f=list(map(int,f[0]))
k=int(f[1])
c=0
for i in f:
      if(i==k):
          c=c+1
print(c)
