e=input()
e=list(e)
c=0
for i in e:
      if(i.isalpha()):
             c=c+1
if(c==0):
      print("yes")
else:
      print("no")
