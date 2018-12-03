def evenodd(n):
    l1=[]
    es=0
    os=0
    for x in n:
        l1.append(x)
        if x%2==0:
            es=es+x
        else:
            os=os+x
    return l1,es,os



l,y,z=evenodd(eval(input("Enter the int values of list:")))
print("original list is:",l)
print("sum od even integers of list is",y)
print("sum of odd integers of list is",z)
