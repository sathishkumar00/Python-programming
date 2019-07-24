l=input()
m=[]
for i in range(0,len(l),2):
           n=l[i]*int(l[i+1])
           m.append(n)
print(*m,sep="")
