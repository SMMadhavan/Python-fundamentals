# Chronologically python file no.14

'''
Going further with the concept of tradeoffs between logic and complexity in programming so that
space and time complexity can be interpreted in system computation and functionality.....

Time and space complexity are the standard metrics used to measure the efficiency of a computer program or algorithm. 
Instead of measuring time in seconds or space in bytes (which vary by machine), these metrics use Big O Notation to describe
how a program's resource needs grow as the input size () increases. 

1. Time Complexity
Time complexity estimates the number of operations an algorithm performs relative to its input size. It measures the "rate of growth" rather than the actual speed in milliseconds. 

O(1) - Constant Time: The operation takes the same amount of time regardless of input size (e.g., accessing an array index).
O(log N) - Logarithmic Time: The problem size is halved with each step, common in Binary Search Algorithms.
O(N) - Linear Time: Execution time grows directly in proportion to input size (e.g., a single loop through a list).
O(N²) - Quadratic Time: Execution time grows exponentially with the square of the input, typical of nested loops (e.g., Bubble Sort). 

2. Space Complexity
Space complexity measures the total memory required by an algorithm during execution. It is composed of two parts: 

Input Space: Memory needed to store the input values.
Auxiliary Space: Extra or temporary memory used by the algorithm, such as recursion stacks or temporary variables. 

Common Examples:
O(1): Using a fixed number of variables regardless of input size.
O(N): Creating a new list that mirrors the size of the input list. 

Moving further into system operations and compatibility parameters. There are certain pre existing parameters, which can 
be inferred for understanding this:
Firstly, the binary parameter...
Secondly,
'''
