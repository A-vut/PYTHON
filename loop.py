list1=['hello', 5,6,2,'W','o','r','l','d',3,7]

print(len(list1))
for i in range(0,10,+2):
    print(list1[i])
else:
    print("Loop finished")
for i in list1:
    print(i)
    if i=='l':
        print("Loop breaked")
        break
else:
    print("Loop Finished")
print("While Loop...... with nested loop\n")
list2=['10','hel','rld']

i=0
while(i<len(list1)):
    for j in list2:
        print(j)
    i+=1
