x = "awesome"
y=9
def myfunc():
  #x = x +"fantastic" #Will raise an error
  global x
  x = x +" fantastic"
  #y=y+6           #Will raise an error
  global y
  y=y+5
  z=90

myfunc()
print(y)
print("Python is " + x)
# print(z)    #Will raise an error
