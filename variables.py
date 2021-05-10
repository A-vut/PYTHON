a=100
b=2.5
c="hello"
d='world'
e='H'
f=g=d
print("a = ",a)
print("b = ",b)
print("c = ",c)
print("d = ",d)
print("e = ",e)
print("f = ",f)
print("Types are: ")

print("a = ",type(a))
print("b = ",type(b))
print("c = ",type(c))
print("d = ",type(d))
print("e = ",type(e))
print("f = ",type(f))

print("\nString operations.......")
s="Hello World!"
print (s)          # Prints complete string
print (s[0])       # Prints first character of the string
print (s[2:7])     # Prints characters starting from 3rd to 5th
print (s[3:])      # Prints string starting from 3rd character
print (s * 2)      # Prints string two times
print (s + "TEST") # Prints concatenated string

print("\nLists operations.......")
list1=["Hello", 5,7.8,'H', "World"]
list2=["hi", 123]
print (list1)          # Prints complete list
print (list1[0])       # Prints first element of the list
print (list1[1:3])     # Prints elements starting from 2nd till 3rd 
print (list1[2:])      # Prints elements starting from 3rd element
print (list2 * 2)      # Prints list two times
print (list1 + list2)  # Prints concatenated lists

print("\nTouples operations.......")
"""Lists elements and size can be changed,
 while tuples are enclosed in parentheses ( ( ) )
  and cannot be updated. Tuples can be thought of as
   read-only lists"""

tuple1 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tuple2 = (123, 'john')

print (tuple1)              # Prints the complete tuple
print (tuple1[0])           # Prints first element of the tuple
print (tuple1[1:3])         # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple1[2:])          # Prints elements of the tuple starting from 3rd element
print (tuple2 *2)           # Prints the contents of the tuple twice
print (tuple1 + tuple2)     # Prints concatenated tuples

# tuple[2] = 1000    # Invalid syntax with tuple
# list[2] = 1000     # Valid syntax with list

print("\nTouples operations.......")
dict={}
dict['a']=5
dict[3]='three'
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(dict)               #print the full dictionary
print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values
print(dict.keys())
print(dict.values())