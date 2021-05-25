class Parent:
    def __init__(self,name):
        print("Perent class __init__",name)
    
class Parent2:
    def __init__(self,name):
        print("Perent2 class __init__",name)
    
class Child(Parent2,Parent):
    def __init__(self):
        print("Child class __init__")
        Parent.__init__(self, "Mehedi")
        Parent2.__init__(self, "Hasan")
        # super().__init__("Mehedi")

child=Child()
print(Child.__mro__) #Method resolution order 

    