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

'''
