#Day 7 Learning operators 

print(5+6) #Addition Operator
print(15-6) #Subtraction Operator
print(15*6) #Multiplication Operator
print(15/6) #Division Operator
print(15//6) #Floor Division Operator (returns whole integer)
print(5%3) #Modulo Operator (returns remainder)
print(2**4) #Exponential Operator (returns power times multiplication)

#Day 8 Building a Static calculator

a=20
b=10
print("The value of", a, "+", 10, "is", a+b)
print("The value of", a, "-", 10, "is", a-b)
print("The value of", a, "*", 10, "is", a*b)
print("The value of", a, "/", 10, "is", a/b)

#Dynamic Approach
a=int(input("First Number:"))
b=int(input("Second Number:"))
print("The value of a+b is:",a+b)
print("The value of a-b is:",a-b)
print("The value of a*b is:",a*b)
print("The value of a/b is:",a/b)

#Day 9 Typecasting

'''
Typecasting is the process of converting one data type to another data type. We have two types of typecasting:
one is implicit typecasting and the other is explicit typecasting. Implicit typecasting is done by the compiler itself
and explicit typecasting is done by the programmer as per his requirement.
'''

#Explicit Typecasting
a="10"
b="20"
print(a+b) #Output: 1020
print(int(a)+int(b)) # Implementing ET, Output: 30

#Implicit Typecasting
num_int = 123   # Integer type
num_float = 1.23  # Float type

# Adding integer and float
result = num_int + num_float

print("Data type of num_int:", type(num_int))
print("Data type of num_float:", type(num_float))
print("Data type of result:", type(result))
print("Result of addition:", result)