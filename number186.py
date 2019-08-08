c=int(input())
if(c==2):
     d,e=list(map(int,input().split(" ")))
     f,g=list(map(int,input().split(" ")))
     h=d*g
     k=e*f
     l=h+k
     print(l)
else:
     d,e,f=list(map(int,input().split(" ")))
     g,h,k=list(map(int,input().split(" ")))
     l,m,n=list(map(int,input().split(" ")))
     p=d*h*n
     q=f*h*l
     r=p+q
     print(r)
