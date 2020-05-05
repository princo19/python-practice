class test:
    def A(self):
        print("insise a")
        self.B()
    def B(self):
        print("inside b")
        print("calling a")
        
ob1=test()
ob1.A()
