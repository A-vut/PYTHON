#Declaration of set
# s1={1,2,'r','d','p',5,9,'q',3,7,'g','a'}
# print(s1)
# print(type(s1))
# #size
# print(len(s1))
# #declaring with constructor
# s2=set(('d','p',5,9,'q')) #must need 2 parenthesis
# print(s2)

#Access Items in Set
# s1={1,2,'r','d','p',5,9,'q',3,7,'g','a'}
# for x in s1:
#     print(x)
# print('a' in s1)
# print('z' in s1)

# #Python - Add Set Items
# s2={'d','p',5,9,'q'}
# s2.add(19)      #Single item
# s2.add(92)
# print(s2)

# s3={44,33,'rr','dd'}
# s2.update(s3)               #add another set with a set
# print(s2)

# l1=['WW','PP',999,888,444,'QQQ',33]
# s3.update(l1)               #add a list with with a set (skips duplicate)
# print(s3)

#Python - Remove Set Items
# s1={1,2,'r','d','p',5,9,'q',3,7,'g','a'}
# # s1.remove(5)                #will raise an error if it is not in the set
# # print(s1)
# # try:
# #     s1.remove(5)
# # except KeyError as ke:
# #     print("Key item : {} is not in the set".format(ke))
# print(s1)
# s1.discard(2)           #will not raise any error if it is not in the set
# print(s1)
# s1.discard(2)
# print(s1)

#can also use pop(), clear() and del

#Join of sets
#Both union() and update() will exclude any duplicate items.
# s1={1,2,'r','d','p',5,9,'q',3,7,'g','a'}
# s2={'d','r','s',4,8,'u'}
# s3=s1.union(s2)
# print(s3)
# s3=s1
# s3.update(s2)
# print(s3)

#intersection_update() method will keep only the items that are present in both sets.
# s3=s1

# s3.intersection_update(s2)
# print(s3)

#intersection() method will return a new set\, empty set otherwise
# s3=s1

# s4=s3.intersection(s2)
# print(s4)

#symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
# s1={1,2,'r','d','p',5,9,'q',3,7,'g','a'}
# s2={'d','r','s',4,8,'u'}
# s3=s1
# s3.symmetric_difference_update(s2)
# print(s3)

#symmetric_difference() method will return a new set, empty otherwise
# s3=s1
# s4=s3.symmetric_difference(s2)
# print(s4)

#difference() method returns a set contains items that exist only in the first set, and not in both sets.
# s3=s1
# s4=s3.difference(s2)
# print(s4)

#difference_update() method shows items that exist only in the first set, and not in both sets.
# s3=s1
# s3.difference_update(s2)
# print(s3)

#isdisjoint() method returns True if none of the items are present in both sets, false otherwise
# s1={1,2,'r','d','p',5,9,'q',3,7,'g','a'}
# s2={'d','r','s',4,8,'u'}

# print(s1.isdisjoint(s2))

#issubset() method returns True if all items in the set exists in the specified set, false otherwise
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}

# print(x.issubset(y))
# print(y.issubset(x))

#issuperset() method returns True if all items in the specified set exists in the original set, false otherwise

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

print(x.issuperset(y))
print(y.issuperset(x))


