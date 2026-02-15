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
2. Bottom-Up Approach (Tabulation)
Tabulation involves solving the problem iteratively from the base cases up to the desired n, typically using an array (or list in Python) to store the intermediate results. 

Python Code
def fibonacci_tabulated(n):
    """
    Calculates the nth Fibonacci number using tabulation.
    """
    if n <= 1:
        return n

    # Create a DP table (list) to store the values
    dp = [0] * (n + 1)
    dp[1] = 1 # Initialize base case

    # Iterate and fill the table
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# Example usage:
n = 10
print(f"The {n}th Fibonacci number (tabulated) is: {fibonacci_tabulated(n)}") # Output: 55
This approach avoids recursion overhead and is often more space-efficient in complex problems. 
'''

'''
# An analogy to understand dynamic programming logic
Python's dynamic typing is like a versatile kitchen where containers are not assigned to ingredients in advance. 
Rather than permanently labelling a jar as “sugar”, you can put honey or salt in it as and when required. 
In Python, you need not declare a variable's data type in advance.
'''

'''
To become a "pro" in dynamic programming (DP) using Python, you must focus on understanding core algorithmic principles and apply specific Python coding practices. 
Mastering Dynamic Programming Fundamentals
The key to dynamic programming is breaking down complex problems into smaller, overlapping subproblems and storing the solutions to avoid redundant computations. 
Master Recursion first: DP solutions are fundamentally optimized recursive solutions. Ensure you are comfortable writing pure, brute-force recursive functions before applying DP.
Identify Overlapping Subproblems and Optimal Substructure: A problem can be solved with DP if it has:
Overlapping Subproblems: The same subproblems are solved multiple times.
Optimal Substructure: The optimal solution to the main problem can be constructed from optimal solutions to its subproblems.
Formulate the Recurrence Relation: This mathematical relationship defines how a solution to a problem is built from solutions to its subproblems. This is the heart of the DP approach.
Learn Memoization (Top-Down): This involves storing the results of expensive function calls in a dictionary or array (memo) and reusing them when the same inputs occur again. This is typically the first step in optimizing a recursive solution.
Learn Tabulation (Bottom-Up): This is an iterative approach where you fill a table (often an array) with solutions starting from the base cases up to the final solution. This avoids the maximum call stack size limitation of recursion in Python.
Optimize Space Complexity: After getting a working solution, consider if you can reduce memory usage by only storing the necessary previous states (e.g., in the Fibonacci sequence, you only need the two previous numbers, not the entire list).
Practice with Classic Problems: Solve a variety of well-known DP problems such as the Fibonacci sequence, Knapsack problem, Longest Common Subsequence, and Edit Distance on platforms like LeetCode, HackerRank, and [GeeksforGeeks](https://www.geeksfor Geeks.org/). 
Leveraging Python's Strengths
Becoming a "pro" also means writing idiomatic, efficient, and clean Python code. 
Use built-in data structures wisely:
Use sets or dictionaries for fast O(1) average time complexity membership testing and lookups, which is crucial in memoization.
Use list comprehensions for creating and filtering lists efficiently and concisely.
Optimize Performance:
Leverage Python's highly optimized built-in functions like sum(), max(), min(), and map() instead of writing custom loops when possible.
Use generators for large datasets to optimize memory usage by producing values on the fly.
Use the .join() method for string concatenation, as using the + operator repeatedly is less efficient.
Minimize the use of global variables in performance-critical sections, as local variables are accessed faster.
Read and Analyze Code: Reviewing well-written open-source projects or solutions from other experienced developers exposes you to new techniques and best practices.
Build a Portfolio and Engage with the Community: Apply your skills to real-world projects and participate in communities like Stack Overflow or relevant subreddits to get insights and collaborate. 
'''
