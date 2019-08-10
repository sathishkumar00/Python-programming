c=list(input())
d=['a','e','i','o','u']
e=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
f=0
for i in range(len(c)-1):
           if(c[i] in e and c[i+1] in d):
                f+=1
           elif(c[i] in d and c[i+1] in e):
                f+=1
if((c[-1] in e and c[-2] in d) or (c[-1] in d and c[-2] in e)):
      f+=1
print(f)
            
