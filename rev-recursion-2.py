def nr(n):
    if n==1:
        return 1
    else:
        return nr(n-1)*n
        






y=nr(eval(input("Enter the number:")))
print(y)
