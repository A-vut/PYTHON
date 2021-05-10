import re


txt="This is our text file where main text is written, and we\
 will searexpch all the pattern in this expression text. Numbexpers are : 98765434567897\
 A regexpexpular expression is text a special sequence\
 of characters that helps you text match or find\
 other strexpings or sets of text expression stringfs, using a\
 specialized syntax held expression in a pattern."

#print(len(txt))

x=re.search("^This.*pattern\.$",txt)
#print(x)

x=re.findall("pattern",txt)
#print(x)

x=re.findall("Portugal",txt)  #No match, so return an empty list
#print(x)

x=re.search("\s",txt)  #here \s is for white space to search

#print("First space was found at position :", x.start())


x=re.split("\s",txt,5) #will split every word using space, we can use other patterns also to split.

#print(x)               # can use number I want to split


x=re.sub("\s"," <space> ",txt) #sub the string with the given pattern
#print(x)


x=re.sub("\s"," <space> ",txt,10) #number of times I want to sub
#print(x)

x=re.search(r"\bs\w+",txt) #search a word which beggining is s 
try:
    print(x.string)         #returns the string that was passed through the function
except:
    print("No match found in string and an attribute error occured.")

x=re.search(r"\bs\w+",txt)
try:
    print(x.span())           #Print the position (start- and end-position) of the first match occurrence, error otherwise
except:
    print("No match found in span and an attribute error occured.")

y=re.search(r"\bs\w+",txt)
try:
    print(y.group())           #Print the part of the string where there was a match. error otherwise
except:

    print("No match found in group and an attribute error occured.")

x=re.findall("[a-zA-Z \.]",txt)     #Find all charachter between a-z and A-Z and <space> and dot(.) also.
#print(x)

x=re.findall("\d",txt)              #Find all digits if matched, empty list otherwise 
#print(x)
x=re.findall("t..t",txt)
#print(x)

x=re.findall("^This.*pattern.$", txt)      #a string starting with This and ending with pattern.     
#print(x)

x=re.findall("(rn)+",txt)
#print(x)


x=re.findall(r"\bexp",txt)                  #at the beggining of the word
#print(x)

x=re.findall(r"ion\b",txt)                  #at the end of the word
#print(x)

x=re.findall(r"\Bexp",txt)                  #find string that contain pattern but not at thr beginning
#print(x)

x=re.findall(r"exp\B",txt)                  #find string that contain pattern but not at thr end
print(x)