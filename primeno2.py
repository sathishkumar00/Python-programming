p=input()
l=[]
p=p.split(" ")
q=int(p[0])
r=int(p[1])
for i in range(q+1,r):
      s=i
      flag=0
      for j in range(2,(s//2)+1):
            if(i%j==0):
                  flag=1
                  break
      if(flag==0):
            l.append(i)
print(*l,sep=" ")
