g=int(input())
h=list(map(int,input().split(" ")))
for i in range(0,len(h)):
       if(h.count(h[i])==1):
              print(h[i])
