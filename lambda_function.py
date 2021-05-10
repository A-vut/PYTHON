# Use lambda functions when an anonymous function is required for a short period of time.
# you have a function definition that takes one argument,
#  and that argument will be multiplied with an unknown number

def function(b):
    return lambda a: a+b

myaddition1 = function(10)
myaddition2 = function(40)

print(myaddition1(15))
print(myaddition2(20))



