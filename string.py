str="Hello world......"
print(str.find("wo"))
print(str.find("wol"))

print(str.index("rl"))
try:
    print(str.index("rlx"))
except:
    print("Not found")

print(str.isalnum())
str="200mnbvcxzasdfgh"
print(str.isalnum())

print(str.isalpha())
str="qwertyu"
print(str.isalpha())

str="+"
seq=("w","r","l","d")
print(str.join(seq))

str="Hello"
print(str.ljust(10,"M"))