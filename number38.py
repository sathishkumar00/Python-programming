f=input()
g=[]
f=f.split(" ")
f=list(map(int,f))
l=f[0]
r=f[1]
for i in range(1,l*r+1):
      if(i%l==0 and i%r==0):
          print(i)
          break
