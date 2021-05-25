class Base:
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return self.name

class Child(Base):
    def __init__(self, name,age):
        self.age=age
        Base.__init__(self,name)
        # super().__init__(name)
    def get_age(self):
        return self.age

class GrandChild(Child):
    def __init__(self,name,age,address):
        self.address=address
        Child.__init__(self,name,age)
        # super().__init__(name,age)
    def get_address(self):
        return self.address

g1=GrandChild("Mehedi",25, "Uttara, Dhaka")
print(g1.get_name(),g1.get_age(),g1.get_address())

print(GrandChild.__mro__)

print("Mro of class : ")
class X:
    pass
class Y:
    pass
class Z:
    pass
class A(X,Y):
    pass
class B(Y,Z):
    pass
class C(Z):
    pass
class M(B,C):
    pass
# class M(B,A,C):
#     pass

print(M.mro())



