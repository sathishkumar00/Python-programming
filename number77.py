l=int(input())
m=list(map(int,input().split(" ")))
for i in range(0,len(m)):
                       n=i+1
                       for j in range(n,len(m)):
                           if(m[i]==m[j]):
                                 p.append(m[i])
print(m[0])
