# Continuation of Python Series
# Logically python file no.11

'''
Introduction to Control Flow in Python 

Control flow in Python is the order in which a program's statements are executed, allowing the program to make decisions, repeat actions, and handle different situations. This is achieved using several primary control flow structures: conditional statements, loops, and transfer statements. 

The main types of control flow statements in Python are:

Conditional Statements (for decision-making)
Loop Statements (for repetitive tasks)
Control Flow-Altering Statements (for modifying loop execution)
Exception Handling (for managing errors)
Structural Pattern Matching (for matching a value against several possibilities) 
 
Conditional Statements
These statements execute specific blocks of code based on whether a condition is True or False. 

if statement: The simplest form, which executes an indented code block only if its condition is true.
# Python code
age = 25
if age >= 18:
    print("You are an adult.")
    
if-else statement: Provides an alternative path of execution. If the if condition is False, the else block runs.
# python
number = 7
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

if-elif-else chain: Allows checking multiple conditions sequentially. Only the first condition that evaluates to True has its corresponding block executed.
# Python code
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

Ternary Operator (Short-hand if-else): A concise way to write an if-else statement in a single line, used for simple assignments.
# Python code
result = "Even" if number % 2 == 0 else "Odd"
 
Loop Statements

Loops automate repetitive tasks by executing a block of code multiple times. 
for loop: Iterates over sequences like lists or ranges.
while loop: Continues executing as long as a condition is True, requiring care to avoid infinite loops.
else clause: Can be added to loops to execute code only if the loop completes without a break. 

Control Flow-Altering Statements 

These modify standard loop or function execution: 
break: Terminates the loop entirely.
continue: Skips the current iteration and moves to the next one.
pass: A null operation used as a placeholder.
return: Exits a function and optionally returns a value.
 
'''
