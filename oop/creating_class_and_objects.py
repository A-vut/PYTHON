class MyClass:
    # pass
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def func(self):
        print("Hello, this is",self.name,"and my age is",self.age)

obj1=MyClass("Mehedi Hasan",40)
print(obj1.name)
obj1.func()
print(obj1.age)

# del obj1.age
# obj1.func()
# del obj1



