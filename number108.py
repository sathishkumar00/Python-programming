p=int(input())
q=[]
for i in range(0,p):
    q.append(list(map(int,input().split(" "))))
r=0
s=0
for i in range(0,p):
    for j in range(0,p):
         if(q[i][j]==1):
               if((i!=p-1) and (q[i+1][j]==0)):
                    r=r+1
               if((j!=p-1) and (q[i][j+1]==0)):
                    r=r+1
               if((i!=0) and (q[i-1][j]==0)):
                    r=r+1
               if((j!=0) and (q[i][j-1]==0)):
                    r=r+1
               if(((i==0) and (j==0)) or ((i==p-1) and (j==0)) or ((i==p-1) and (j==p-1)) or((j==p-1) and (i==0))):
                    s=s+1
               elif(i==1 and j>0 and j<p-1 and r==3):
                    s=s+1
               elif(r==4):
                    s=s+1
     r=0
print(s)
