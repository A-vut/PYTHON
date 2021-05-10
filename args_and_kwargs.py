#use of args and kwargs

def student(name, age, *marks):  #here args will receive additional arguments as a tuples
    print("Name :",name)
    print("Age :",age) 
    print("Marks :",marks)
    #print(type(marks))

student("Mehedi", 25,23,65,13,87,98,45,65)

def student(name, age, **marks):  #here **marks will receive additional arguments as a Dictionary with key values
    print("Name :",name)
    print("Age :",age) 
    print("Marks :",marks)
    # print(type(marks))
    print("Marks Obtained : ")
    for keys, values in marks.items():
        print(keys, ':',values)

student("Mehedi", 25, Bangla=23,English=65,Humanities=13,Religions=87,Math=98,Sociology=45,Statistics=65)



