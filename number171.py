p=list(map(int,input()))
q=0
r=[]
for i in range(len(p)-1):
      if((p[i]%2==0 and p[i+1]%2!=0) or (p[i]%2!=0 and p[i+1]%2==0)):
           q=q+1
           r.append(q)
      else:
          q=0
r.append(q)
if(max(r)==0):
      print(max(r))
else:
      print(max(r)+1)
