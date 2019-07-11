p=input()
q=[0]
if "ab" not in p:
       print("0")
else:
     for i in range(len(p)):
          c=1
          for j in range(i,len(p)-1):
             if(p[j]=="a" and p[j+1]=="b"):
                c=c+1
                q.append(c)
             elif(p[j]=="b" and p[j+1]=="a"):
                c=c+1
                q.append(c)
             else:
                q.append(c)
             c=1
             break
          if(p[i]=="a"):
                q.append(c)
          else:
                q.append(c-1)
print(max(q))
