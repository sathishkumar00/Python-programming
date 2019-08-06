l,m=input().split(" ")
l=list(l)
m=list(m)
for i in l:
     if i in m:
         print("true")
         break
     else:
         print("false")
         break
