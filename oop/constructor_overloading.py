# Python does not allow multiple init methon in a class
# if we declare multiple init method, it will take the last one we declared
# If we want to provide difrent number of parameter, we can use default argument concept


class MyClass:
    # def __init__(self):
    #     pass
    # def __init__(self,arg1="Default_Value1"):
    #     self.arg1=arg1
    #     print(arg1)

    def __init__(self,arg1="Default_Value1",arg2="Default_Value2"):
        self.arg1=arg1
        self.arg2=arg2
        print("arg1 = {}. and arg2 = {}".format(arg1,arg2))
        
    # def __init__(self,arg1="Default_Value1",arg2="Default_Value2",arg3="Default_Value3"):
    #     self.arg1=arg1
    #     self.arg2=arg2
    #     self.arg3=arg3
    #     print(arg1)


obj1=MyClass()
obj1=MyClass("Hello")
obj1=MyClass(arg2="Hello")
obj1=MyClass("Hi","Hello")
obj1=MyClass(arg2="Hi",arg1="Hello")