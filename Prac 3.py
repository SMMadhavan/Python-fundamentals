#Day 10 Taking input from user
#(i) String
a=input("Enter your name:")
b=input("Enter your age:")
print("Your name is:",a)
print("Your age is:",b)

#(ii) Integer
a=int(input("Enter your age:"))
b=int(input("Enter your weight:"))
print("Your age is:",a)
print("Your weight is:",b)

c=input("Num 1:")
d=input("Num 2:")
print(c+d) #Output is concatenation of two strings even though we are taking input as numbers
#To avoid this, we can convert the input to int or float
c=int(input("Num 1:"))
d=int(input("Num 2:"))
print(c+d) #Output is addition of two numbers
#or we can also use int in print statement
c=input("Num 1:")
d=input("Num 2:")
print(int(c)+int(d)) #Output is addition of two numbers

#In the same way, we can also take float input
a=float(input("Num 1:"))
b=float(input("Num 2:"))
#Float is a datatype used when numbers involve decimal values and are not whole integer 
print(a+b) #Output is addition of two numbers (Float Value)


