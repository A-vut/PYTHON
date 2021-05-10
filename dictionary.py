# dict1={"H":3,"b":4,6:'abc'}
# print(dict1.keys())
# print(dict1.values())
# dict2={"Hlw":"Hello","IM":"I am","mhd":"Mehedi","age":25,"job":"SE"}
# print(dict2["age"], dict2["job"])
# del dict2["IM"]
# print(dict2)
# for i in dict2:
#     print(i,dict2[i])
# dict3=dict2.copy()
# print(dict3)
# seq1=('Name','Sex','Age')
# seq2=('Mehedi','Male','25')

# dict4=dict.fromkeys(seq1,seq2)
# print(dict4)
# dict4=dict.fromkeys(seq1,15)
# print(dict4)
# print(dict4.get('hi',"Not Found"))

# car={
#     'Brand' : 'Ford',
#     'Model' : 'Mustang',
#     'Year' : 1964
# }
# # print(car.keys(), car.values())
# # print(car['Model'])
# print(car.items())

#Duplicates Not Allowed, duplicate values will overwrite existing values

# car={
#     'Brand' : 'Ford',
#     'Model' : 'Mustang',
#     'Year' : 1964,
#     'Year' : 2009
# }
# print(car['Year'])
# print(len(car))

# car={
#     'Brand' : 'Ford',
#     'Model' : 'Mustang',
#     'Year' : 1964,
#     'Year' : 2009,
#     "Colors": ["Red", "White", "Blue"]
# }
# # print(car)
# x=car.keys()
# print(x)            #before the change
# car['Made in']='Bangladesh'
# print(x)            #after the change

#Check if Key Exists

# if 'model' in car:
#     print("Yes, it exists")
# else:
#     print("No, it\'s not exists")

# Change value of item

# car={
#     'Brand' : 'Ford',
#     'Model' : 'Mustang',
#     'Year' : 1964,
#     "Colors": ["Red", "White", "Blue"]
# }
# # print("Year :",car['Year'])
# car['Year']=2009
# # print("Year :",car['Year'])

# # to use update(), argument must be a dictionary, or an iterable object with key:value pairs

# car.update({'Price':100000000, 'Realesed Date':'21/12/2009'})
# # print(car)
# # print(len(car))

# car.pop('Year')
# print(car)
# car['Year']=2009
# print(car)
# car.popitem()
# print(car)
# car.popitem()       #removes the last inserted item 
# print(car)
# del car['Model']        #can also delete the dictionary completely
# print(car)
# car.clear()             #empties the dictionary
# print(car)

# car={
#     'Brand' : 'Ford',
#     'Model' : 'Mustang',
#     'Year' : 1964,
#     "Colors": ["Red", "White", "Blue"]
# }
# car.update({'Price':100000000, 'Realesed Date':'21/12/2009'})
# print(car)

#Print all key names in the dictionary, one by one
# for x in car:
#     print(x)
# for x in car.keys():
#     print(x)

#Print all values in the dictionary, one by one
# for x in car:
#     print(car[x])
# for x in car.values():
#     print(x)

#Loop through both keys and values, by using the items()

# for x,y in car.items():
#     print(x,':',y)

#Copy a Dictionary
# cannot copy a dictionary simply by typing dict2 = dict1,
# because: dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.

# car1=car.copy()
# print(car1)
# car2=dict(car)
# print(car2)

# Nested Dictionary 
# family={
#     'child1' : {
#     "name" : "Emil",
#     "year" : 2004
#     },
#     'child2' : {
#     "name" : "Tobias",
#     "year" : 2007
#     },
#     'child3' : {
#     "name" : "Linus",
#     "year" : 2011
#     }
# }
# print(family)
# print(family['child1']['year'])

# family['child4']={'name': 'Hasan', 'year': 2012, 'age': 11}
# # print(family)
# # for x in family:
# #     print(x,':',family[x])

# for member in family.keys():
#     print(member,':')
#     #print(type(member))
#     for x in family[member]:
#         print(x,':',family[member][x])


car={
    'Brand' : 'Ford',
    'Model' : 'Mustang',
    'Year' : 1964,
    "Colors": ["Red", "White", "Blue"]
}
car.update({'Price':100000000, 'Realesed Date':'21/12/2009'})
print(car)

# setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value

x=car.setdefault('Model', 'mmmm')   
print(x)
x=car.setdefault('Availabe','Yes')
print(x)
print(car)


