p,q=map(eval,input().split(" "))
r=[]
for i in range(p):
     r.append(list(map(eval,input().split(" "))))
s=[]
t=[]
a=[]
b=[]
c=0
d=0
t.append(r[c][d])
s.append([c,d])
while[p-1,q-1] not in pos:
     c=0
     for i in pos:
        if(i[0]+1<p and i[1]+1<q):
           a.append(r[i[0]+1][i[1]]+out[k])
           a.append(r[i[0]][i[1]+1]+out[k])
           b.append(r[i[0]+1,i[1]])
           b.append(r[i[0],i[1]+1])
         elif(i[0]+1<p):
           b.append(r[i[0]+1][i[1]]+out[k])
           b.append([i[0],i[1]+1])
         elif(i[1]+1<q):
           b.append(r[i[0],[i[1]+1])
           b.append([i[0]+1,i[1]])
         c+=1
s=b
b=[]
t=a
a=[]
print(max(t))
