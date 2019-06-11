p=input()
p=p.split(" ")
p=list(map(int,p))
q=p[0]+p[1]
if(q%2==0):
     print("even")
else:
     print("odd")
