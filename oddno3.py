p=input()
l=[]
p=p.split(" ")
p=list(map(int,p))
n=p[0]
k=p[1]
q=input()
q=q.split(" ")
q=list(map(int,q))
for i in q:
     if(i%2!=0):
          l.append(i)
print(l[k-1])
