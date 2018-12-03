class Student:
    def __init__(self):
        self.rollno=0
        self.name=""
        self.semester=0
        self.branch=""

    def f1(self,w,x,y,z):
        self.rollno=w
        self.name=x
        self.semester=y
        self.branch=z
        

t1=Student()
t1.f1(input("enter rollno:"),input("enter name:"),input("enter semester:"),input("enter branch:"),)

print(t1.rollno,t1.name,t1.semester,t1.branch)
