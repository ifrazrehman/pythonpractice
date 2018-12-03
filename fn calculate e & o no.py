def cal():
    e=0
    o=0
    l1=[1,2,3,4,5,6,7,8,9,10]
    for x in l1:
        if x%2==0:
            e=e+x
        else:
            o=o+x
    

    print("The sum of even numbers in list is:",e)
    print("The sum of odd numbers in list is:",o)    
    

cal()

