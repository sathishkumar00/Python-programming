c=input().split(" ")
e=[]
f=""
if(len(c)>1):
      f+=c[0]+" "
      for i in range(1,len(c)-1):
           d=c[i]
           d=d[::-1]
           e.append(d)
      for i in e:
         f+=i+" "
      f+=c[-1]
      print(f)
else:
   print(*c)
