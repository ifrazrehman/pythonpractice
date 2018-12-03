x=int(input("Enter the numenator:"))
y=int(input("Enter the denomenator:"))

try:
   z=x/y
   print("the result is:",z)
except( ZeroDivisionError,TypeError,ValueError):
    print("somethings wrong in division")

except:
     print("Default Exception")

else:
    print("this line print in else block")

finally:
    print("this is line is in final block")

print("this is the last line of program")


