f1=open("test.txt","w")
f1.write("Hello there, this is a test file.\nHere we will test different mode of file.\nWe also test basic operations of file.\nsesson 2.......\nHello there, this is a test file.\nHere we will test different mode of file.\nWe also test basic operations of file.")
f1.close()
f2=open("test.txt","r")

# x=f2.readline()
# print(x)
# x=f2.readline()
# print(x)
# x=f2.readline()
# print(x)
for line in f2:
    print(line, line[3], line[10])
#x=f2.read()
#print(x)
#f2.close()
print("\nName of the file:",f2.name)
print("Closed or not:",f2.closed)
print("Open mode of the file:",f2.mode)
