class xyz:
    name=" "
    age=0
    def __init__(self):
        print("inside constructor")
        self.name="ajay"
        self.age=40
    def show(self):
        print(self.name, "\n" ,self.age)
ob1=xyz()
ob1.show()
