try:
    print("this is line of 1st try block statement")
    print("this is line of 2nd try block statement")
    3/"5"
    print("this is line of 3rd try block statement")

    try:
        3/0
        print("this is line of nested try block")
        print("this is line of nested try block")
    except ZeroDivisionError:
        print("except 1")
    finally:
        print("finally1")
    print("Line 5")
except TypeError:
    print("Except2")
finally:
    print("Finally 2")
        
