p=input()
p=p.replace(" ","")
l=[]
for i in range(0,len(p)):
       q=i+1
       for j in range(q,len(p)):
            if(p.count(p[i])==1):
                  l.append(p[i])
                  break
print(*l,sep="")
