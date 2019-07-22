d=input()
e=[]
f=0
for i in d:
      if(int(i)%2!=0):
           e.append(int(i))
      else:
           print("E")
for i in e:
     f=f+i
if(f%2==0):
     print("E")
else:
     print("O")
