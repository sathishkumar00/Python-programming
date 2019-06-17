def function(f):
        if(f==0):
            return False
        while(f!=1):
             if(f%2==0):
                  return False
             f=f//2
        return True
f=int(input())
if(function(f)):
       print("yes")
else:
       print("no")
