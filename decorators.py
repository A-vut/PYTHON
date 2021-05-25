# def hello_decorator(func):
#     print("Before entering inner1")
#     def inner1():
#         print("Hello, this is inner 1 before function execution")
#         func()
#         print("This is after function execution")
#     print("Before returning inner1")
#     return inner1

# def function_to_be_used():
#     print("This is the main function that is to be executed")

# print("Calling decorator")
# X=function_to_be_used
# # function_to_be_used=hello_decorator(X)
# print(function_to_be_used)
# print("Before calling function_to_be_used")
# function_to_be_used()

def uppercase_decorator(function):

    # print("1. Entered into decore",type(function))
    def wrapper():
        func = function()
        # print("3. Value of func :",func)
        make_uppercase = func.upper()
        # print("4. value of make_uppercase :",make_uppercase)
        return make_uppercase
    # print("2. returning wrapper from decor")
    return wrapper
def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

#order of execution of decorator is bottom up
@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'

# print("0. start from here")
# decorate = uppercase_decorator(say_hi)
# print("0.1. start from here 2",decorate,type(decorate))
# print(decorate())
print(say_hi())




