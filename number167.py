p,q=map(int,input().split(" "))
r=[]
for _ in range(p):
     r.append(input())
for j in range(len(r)):
     if('0' in r[j]):
          r[j]=r[j].replace("0","")
     r[j]=r[j].replace(" ","")
s=[]
for j in r:
     if(len(j)>0):
           s.append(len(j))
q=min(s)
t='1 '*q
t=t.strip()
for j in range(q):
        print(t)
