g=input()
g=g.split(" ")
n=g[0]
k=g[1]
h=input()
h=h.split(" ")
c=0
for i in range(0,len(h)):
             for j in range(i+1,len(h)):
                   if(i==j):
                        l=i
                        c=c+1
                        if(c==k):
                           print(l)
