l,m=list(map(int,input().split(" ")))
n=list(map(int,input().split(" ")))
n.sort(reverse=True)
p=0
for i in n:
        if(m==0):
             break
        q=m//i
        p+=q
        m=m-i*q
print(p)
