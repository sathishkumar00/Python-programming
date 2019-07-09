p=input().split(" ")
l=[]
if(len(p)==1):
       q=p[0]
       print(q[ ::-1])
elif(len(p)>1):
       for i in p:
           l.append(i[ ::-1])
print(*l,sep=" ")
