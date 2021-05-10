
try:
    a=int(input("Enter an integer: "))
    b=int(input("Enter an integer: "))
    print(f"The division of {a} by {b} is: {a/b}")
except ZeroDivisionError as e:
    print("Second number Can't be 0.")
except ValueError as e:
    print("Number Must be an Integer")
except Exception as e:
    print("Something went wrong, try again with different input.")
finally:
    print("Thanks for using.")
