p=int(input())
q=list(map(int,input().split(" ")))
for i in range(0,len(q)):
       r=i+1
       for j in range(r,len(q)):
           if(q[i]==(-q[j])):
                print(q[i],q[j])
           elif(q[i]==0 and q[j]==0):
                print(q[i])
