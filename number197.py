c=int(input())
d=list(map(int,input().split(" ")))
e=[]
f=""
for i in d:
      e.append(d.count(i))
e=list(map(str,e))
f+="".join(e)
g=min(e)
h=f.find(str(g))
print(d[h])
