# tup1=("hello","how","are","you", 4,1,6,3)
# tup2=(9,8,5,3,"i","am","fine")
# print(tup1)
# print(len(tup2))
# tup3=("Hi","My","name",3,4,2,"is")
# print(tup3[5])

# try:
#     del(tup3[5])
# except:
#     print("Touples can't be modified")
# tup4=(5,)
# print(tup4)
# del tup4
# # print(tup4)
# list1=["hi","ki","koro","muri","khao"]
# #print(list1)
# tup4=tuple(list1)
# #print(tup4)

# #Tuple declaration
# print("Tuple declaration")
# tp1=("apple", "banana", "cherry")
# print(tp1)
# #length
# print(len(tp1))
# #type
# print(type(tp1))
# #tuple constructor
# tp2=tuple(("hi","ki","koro","muri","khao"))    #must use double paranthesis
# print(tp2)

#Access Tuple Items
# print("Access Tuple Items")
# print(tp2[3])
# print(tp2[-1])
# print(tp2[1:4])
# print(tp2[1:])
# print(tp2[:4])
# print(tp2[-3:-1])
# print(tp2[:-2])
# print(tp2[-3:])

#Check if Item Exists
# if "koro" in tp2:
#     print("yes, it exists.")

# #delete tuple
# temp=tp2
# print(temp)
# del temp
#print(temp)

#Python - Unpack Tuples
# fruits = ("apple", "banana", "cherry")
# (a,b,c) = fruits
# print(a)
# print(b)
# print(c)
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (a,*b,c) =fruits
# print(a)
# print(b)
# print(c)

# for x in fruits:
#     print("for index :",x)
    
# for i in range(len(fruits)):
#     print("for index :",fruits[i])

# i=0
# while i<len(fruits):
#     print("while :", fruits[i])
#     i+=1

#Python - Join Tuples
f1= ("apple", "banana", "cherry")
f2=("strawberry", "raspberry")
f3=f1+f2
print(f3)

f2=f1*3
print(f2)

#Tuple Methods
tp1=(91,92,65,83,74,65,56,67,78,89,99,65,34,43,23,34,91)
print(tp1.count(65))
print(tp1.count(999))

print(tp1.index(65))
try:
    print(tp1.index(999))
except ValueError as ve:
    print(ve)

