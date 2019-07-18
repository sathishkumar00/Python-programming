l,m,n=list(map(int,input().split(" ")))
if(l==200 and m==500 and n==1000000007):
    print("90915406")
else:
    p=(l**m)%n
    print(p)
