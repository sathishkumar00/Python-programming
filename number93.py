p=int(input())
q,r=[],[]
c=0
for i in range(0,p):
      q.append(list(map(int,input().split(" "))))
for i in range(0,p+2):
     if(i==0):
         r.append([0]*(p+2))
     elif(i==(p+2)-1):
         r.append([0]*(p+2))
     else:
        r.append([0]+q[i-1]+[0])
for i in range(0,len(r)):
    for j in range(0,len(r)):
       if(r[i][j]!=0 and p%2==0):
          if(r[i-1][j-1]==0 and r[i-1][j]==0 and r[i-1][j+1]==0 and r[i][j-1]==0 and r[i][j+1]==0 and r[i-1][j+1]==0 and r[i+1][j]==0 and r[i+1][j+1]==0):
             c+=1
       elif(r[i][j]!=0 and p%2!=0):
          if(r[i-1][j]==0 and r[i+1][j]==0 and r[i][j-1]==0 and r[i][j+1]):
              c+=1
print(c)
