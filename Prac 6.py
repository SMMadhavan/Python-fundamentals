# Learning python utilities and libraries 

'''
"Python utilities" generally refers to either the powerful built-in standard library modules for common tasks, 
the practice of writing reusable "utility functions" in a codebase, or third-party libraries designed for
general-purpose helpers. 
'''

'''
Standard Library Utility Modules
Python's extensive standard library provides modules to handle a wide range of common tasks without needing external packages. These can often be run directly from the command line using python -m [module_name]. 
File System & OS Interaction: The os, os.path, and shutil modules manage files and directories, such as copying files (shutil.copy), listing directories (os.listdir), and creating paths (os.path.join).
Running External Processes: The subprocess module allows for executing external commands and capturing their output.
Networking and HTTP: The urllib.request module fetches data from URLs. For more advanced use, the popular third-party requests library is widely used.
Debugging and Profiling:
pdb: The standard Python debugger for step-by-step code execution.
cProfile: A built-in profiler to identify performance bottlenecks in your code by measuring function call times.
Command-line Tools: Modules like json.tool, http.server, and calendar can be run as simple command-line utilities for tasks like pretty-printing JSON, starting a local web server, or viewing a calendar. 
Custom "Utility" Functions in Projects
In software development, "utility functions" are small, reusable pieces of code that perform generic tasks not specific to the application's core business logic. 
Common Use Cases: String manipulation, password hashing (e.g., in a PasswordUtils class), date and time operations, or data formatting are typical examples.
Organization: These functions are typically grouped into a utils.py module to keep the main codebase clean and organized. 
Third-Party Utility Libraries
Several third-party packages are available to provide additional helper functions. 
python-utils: A collection of functions and classes for common patterns, installable via pip install python-utils. It offers tools for things like converting text to numbers or ensuring consistent string formats.
pyxx: A library offering a unit converter, array tools, and file processing operations, installable via pip install pyxx. 
'''

'''
Python functions are named blocks of reusable code designed to perform a specific, related action. They enhance modularity and code reuse, making programs easier to manage, debug, and understand. 
Defining and Calling Functions
Functions are defined using the def keyword, followed by a name, parentheses for potential parameters, and a colon. The body of the function must be indented. 

#example: 
def greet(name):
  """This function greets the person passed in as a parameter.""" # Docstring
  print(f"Hello, {name}!")

A function is executed when it is called by its name, with any required arguments passed within the parentheses: 
greet("Alice") # Calling the function
# Output: Hello, Alice!

Key Concepts
Arguments and Parameters: Parameters are placeholders defined in the function definition, while arguments are the actual values passed to the function when it is called.
The return Statement: The return statement is used to exit a function and optionally send a value back to the caller. If no value is returned, the function implicitly returns None. A function can return multiple values, which Python packs into a tuple.
Scope: Variables defined inside a function are local to that function's scope and cannot be accessed from outside. Variables defined outside a function have a global scope and can be accessed within the function.
Indentation: Python uses indentation to define code blocks, including the body of a function. All statements within the function must have the same level of indentation. 

Types of Python Functions
Python supports several types of functions:
User-defined Functions: Functions created by developers to perform specific tasks, like the greet function above.
Built-in Functions: Functions that are pre-defined and always available in the Python interpreter (e.g., print(), len(), sum(), max(), min(), abs()). You can find a complete list in the Python documentation.
Lambda (Anonymous) Functions: Small, unnamed functions defined using the lambda keyword. They can take any number of arguments but must have only one expression.
Recursive Functions: Functions that call themselves to solve a problem, typically involving a base case to prevent infinite recursion. 

Types of Arguments
Python allows for flexible ways to pass arguments to functions: 
Positional Arguments: Arguments passed based on their order in the function call.
Keyword Arguments: Arguments identified by their parameter names, allowing them to be passed in any order.
Default Arguments: Parameters that assume a default value if no value is provided in the function call.
Arbitrary Arguments (*args and **kwargs): Used to pass a variable number of non-keyworded (*args) or keyworded (**kwargs) arguments to a function. 
'''
# 
