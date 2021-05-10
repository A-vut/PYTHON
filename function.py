def func(a, b):
    c=a+3;
    d=b-3;
    return c*d

print(func(5,5))

def fib(n):
    if n<0:
        return ValueError
    elif n==0 or n==1 :
        return n
    else:
        return fib(n-1)+fib(n-2)
# for i in range (1,100,+1):
print(fib(6))




