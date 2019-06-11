def print_factors(p):
     for i in range(1,p+1):
        if(p%i==0):
             print(i)
q=int(input())
print(print_factors(q))
