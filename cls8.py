class test:
    def __init__(self,x):
        self.x=x

    def __gt__(self,other):
        print(self.x,other.x)
        return self.x>other.x
    def _lt__(self,other):
        print(self.x,other.x)
        return self.x<other.x

ob1=test(int(input("enter the value:")))
ob2=test(int(input("enter the value:")))
ob3=ob1>ob2
print(ob3)
ob3=(ob1<ob2)
print(ob3)
