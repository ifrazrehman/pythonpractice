def b1(a):
    s=bin(a)
    print("The binary of number:",a,"is",s[::])
    print("The reverse of above binary representation of",a,"is:",s[-1::-1])
b1(8)
