c=input().split(" ")
for i in range(0,len(c)):
      if(c[i]=="and" and len(c)>1):
          c[i-1],c[i+1]=c[i+1],c[i-1]
      elif(len(c)==1):
          break
print(*c,sep=" ")
