e=input()
e=e.split(" ")
e=list(map(int,e))
f=e[0]
g=e[1]
if(f>g):
    smaller=g
else:
    smaller=f
for i in range(1,smaller+1):
         if((f%i==0) and (g%i==0)):
                h=i
print(h)
