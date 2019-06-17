def function(f):
        if(f==0):
            return false
        while(f!=1):
             if(f%2==0):
                  return false
             f=f//2
        return true
f=int(input())
if(function(f)):
       print("yes")
else:
       print("no")
