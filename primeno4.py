f=input()
f=f.split(" ")
f=list(map(int,f))
count=0
for i in range(f[0],f[1]):
     c=0
     for j in range(2,i):
          if(i%j==0):
              c=1
              break
     if(c==0):
          count=count+1
print(count)
