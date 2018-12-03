def prime(num1,num2):
    
    for x in range(num1+1,num2):
        for y in range(2,x):
            if x%y==0:
                break
        else:    
            print(x,"is prime number among series")

prime(int(input("Enter the first range:")),int(input("Enter the seconed range:")))
