l=int(input())
m=[]
for i in range(0,l):
     n=input()
     m.append(n)
p=[]
for i in zip(*m):
    if(i.count(i[0])==len(i)):
        p.append(i[0])    
    else:
        break
print(''.join(p))
