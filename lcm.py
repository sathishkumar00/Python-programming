p=input()
p=p.split(" ")
p=list(map(int,p))
q=p[0]
r=p[1]
if(q>r):
    greater=q
else:
    greater=r
while(True):
    if((greater%q==0) and (greater%r==0)):
          hcf=greater
          break
    greater=greater+1
print(greater)
