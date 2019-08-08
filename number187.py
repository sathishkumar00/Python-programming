c=int(input())
d=input()
e=d
d.replace(" ","")
f=""
for i in e:
      if(i=="0"):
           f=f+i
d+=f
d=list(d)
for i in d:
     if(i==" "):
          d.remove(i)
d.remove(" ")
print(*d,sep=" ")
