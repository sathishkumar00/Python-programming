c='/'
d='%'
p=input()
if c in p:
      p=p.split("/")
      p=list(map(int,p))
      r=p[0]//p[1]
      print(r)
elif d in p:
      p=p.split("%")
      p=list(map(int,p))
      r=p[0]%p[1]
      print(r)
