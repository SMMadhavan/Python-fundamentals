#Day 1 (100 days of learning python)
print("Hello World, It's my first day in learning python")
print(1)
print(3-2)
print(15-14)
print(10/10)
print(0+1)

#Day 2 (Comments and escape sequence characters)
'''
This is a multiline character used to make multiple lines as comment lines
This is line number second
This is line number third
This is line number four
'''
"""
This is a multiline character used to make multiple lines as comment lines
This is line number second
This is line number third
This is line number four
"""
print("I am learning this course from code with harry\nand this is very interesting\talso i am learning new concepts")
print("Hey",5,6, sep="~",end="009\n")# sep is the command used for seperating different values specified in a single print statement; end command tells the interpretor what should be added to the end of a statement and can be specified only once. If \n is not added to end value, the next line also gets printed on the same line.

#Day 3 (Variables & Data types)
a = 10
print(a)
print("The type of a is", type(a))
b="Harry"
print(b)
print("The type of b is", type(b))
c= True
print("The type of c is", type(c))

#Data types can be classified as Integer, Float, String, Boolean, Complex no.s, Lists, tuple and dictionaries
list=[8,2,"list",2.9]
print(list)
tuple=("parrot",34,5.8,"Kings")
print(tuple)
dict={"key1":"value1", "key2":"value2", "key3":"value3"}
# Lists, Tuples, Dictionaries and sets are all important data types which will be covered in detail in numpy,pandas etc

print(dict)#Dictionary values can be retreived by their corresponding keys
