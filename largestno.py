p=input()
p=p.split(" ")
if(int(p[0])>int(p[1]) and int(p[0])>int(p[2])):
     print(int(p[0]))
elif(int(p[1])>int(p[0]) and int(p[1])>int(p[2])):
     print(int(p[1]))
else:
     print(int(p[2]))
