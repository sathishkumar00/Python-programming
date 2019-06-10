p=input()
for i in p:
    if(i.isalpha()):
          q=1
    elif(i.isnumeric()):
          r=1
if(q==1 and r==1):
      print("Yes")
else:
      print("No")
