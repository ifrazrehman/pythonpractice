r=lambda a:1 if a==0 else a*r(a-1)
x=r(int(input("enter 1st no:")))
print("factorial is =",x)
