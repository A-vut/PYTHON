a=5
b=10
c=30
if a>=b and a>=c:
    print(f"a is gtestest and it is {a}")
elif b>=a and b>=c:
    print(f"b is gtestest and it is {b}")
else:
    print(f"c is gtestest and it is {c}")

if a>=b:
    if a>=c:
        print(a)
    else:
        print(c)
elif b>=a:
    if b>=c:
        print(b)
    else:
        print(c)
else:
    print(c)
