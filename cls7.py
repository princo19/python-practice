class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        print(self.x)
        print(other.x)
        return self.x + other.x
    def __sub__(self,other):
        print(self.x)
        print(other.x)
        return self.x - other.x
ob1=A(int(input("enter the value of a:")))
ob2=A(int(input("enter the value of b:")))
ob3=ob1-ob2
ob4=ob1+ob2
print(ob3)
print(ob4)
