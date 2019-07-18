p=input().split(" ")
q=str(p[0])
r=str(p[1])
if(len(q)==len(r)):
        print(*p,sep="")
elif(len(q)>len(r)):
        print(q[ :len(r)]+r)
else:
        print(q+r[ :len(q)])
