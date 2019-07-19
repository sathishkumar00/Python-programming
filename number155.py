p="WELCOMETOGUVICORPORATIONS"
q=input()
r=[]
for i in range(5):
     r.append(list(p[i*5:(i*5)+5]))
s="".join(["".join(k) for k in [[r[i][j] for i in range(5)] for j in range(5)]])
for i in range(len(p)):
         if(p[i:i+len(q)]==q):
               print(i//5,i%5)
               print((i+len(q)-1)//5,(i+len(q)-1)%5)
               break
         if(s[i:i+len(q)]==q):
               print(i%5,i//5)
               print((i+len(q)-1)%5,(i+len(q)-1)//5)
               break
else:
   print("0")
