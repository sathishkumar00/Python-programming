p,q=input().split(" ")
r=abs(len(p)-len(q))
for i in range(0,len(p)):
    if(len(p)==1 and q[i] in p):
        break
    if(p[i]!=q[i]):
        r+=1
print(r)
