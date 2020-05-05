class demo:
    def __init__(self):
        print("inside constructor")

    def __del__(self):
        print("destructor delete all memory")

ob1=demo()
ob2=ob1
ob3=ob1
print(id(ob1))
print(id(ob2))
print(id(ob3))

del ob1
del ob2
del ob3
