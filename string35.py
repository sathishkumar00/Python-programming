p=input()
q=[]
for i in range(0,len(p)):
     q.append(p[i])
for i in range(0,len(q)):
     q[i]=chr(((ord(q[i])+3-64)%26)+64)
print("".join(q))
