list1=["hello", "world","hi",4,1,9,5,'kemon',"acho"]
list2=[0,9,8,7,"hemato","cactus"]
print(list1)
list3=list1+list2
print(list3)
del list1[2]
print(list1)
for i in list2:
    print(i)

list1.append(999)
print(list1)
list1.append(list2)
print(list1)
list1=["hello", "world","hi",4,1,9,5,'kemon',"acho"]
list2=[0,9,8,7,"hemato","cactus"]
list1.extend(list2)
print(list1)
list2.insert(-9,"Inserted Text")
print(list2)
print(len(list2))

print(list2.pop())
print(list2.pop(3))
print(list2)