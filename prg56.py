f=input()
f=f.split(" ")
k=f[1]
for i in f[0]:
         if(i==k):
             print((f[0].index(i))+1)
             break
              
