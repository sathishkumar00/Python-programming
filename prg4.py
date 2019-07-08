l,m=input().split(" ")
n=0
if(len(l)>len(m)):
    l,m=m,l
i=0
while(i<len(l)):
    n+=(ord(m[i]))-(ord(l[i]))
    i+=1
for i in range(i,len(m)):
    n+=ord(m[i])-ord('a')+1
print(n)
