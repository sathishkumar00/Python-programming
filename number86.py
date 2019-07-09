p=int(input())
for i in range(0,p):
      q=2**i
      if(q>p):
          q=2**(i-1)
          break
r=p-q
print(r)
