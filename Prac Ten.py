# Introduction in dynamic programming
'''
Fundamentals in dynamic programming

Dynamic programming is an algorithmic technique that solves problems by breaking them into smaller, overlapping subproblems and storing their solutions to avoid recomputation. A classic beginner's example is calculating Fibonacci numbers efficiently. 
Here are beginner Python codes for the Fibonacci sequence using both major dynamic programming approaches:
1. Top-Down Approach (Memoization) 
Memoization involves using a dictionary or a list (often called memo or dp) to store the results of expensive function calls and returning the cached result when the same inputs occur again. 

Python Code

def fibonacci_memoized(n, memo={}):
    """
    Calculates the nth Fibonacci number using memoization.
    """
    # Base cases
    if n <= 1:
        return n
    
    # Check if the result is already in the memoization table
    if n in memo:
        return memo[n]
    
    # Recursive calls and store the result in the memo table
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    
    return memo[n]

# Example usage:
n = 10
print(f"The {n}th Fibonacci number (memoized) is: {fibonacci_memoized(n)}") # Output: 55
This method is intuitive as it follows the natural recursive definition, but optimizes the redundant computations. 
'''

'''
'''
