p=int(input())
q=input()
l=[]
q=list(q)
for i in q:
     if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
           q.remove(i)
           l.append(i)
r=q[ ::-1]
print(*r,sep="")
