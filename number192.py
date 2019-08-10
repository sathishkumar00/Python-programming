c,d=list(map(int,input().split(" ")))
e=[]
for i in range(0,c):
    e.append(list(map(int,input().split(" "))))
for i in e:
    if d in i:
        print("yes")
        break
else:
   print("no")
