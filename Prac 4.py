#Day 11 Strings in Python

'''Strings are a sequence of characters enclosed in single or double quotes.
Strings are immutable, meaning they cannot be changed after creation.
Strings are indexed, meaning each character in the string has a unique index starting from 0.
Strings can be sliced, meaning we can extract a portion of the string using the index.
Strings can be concatenated, meaning we can join two or more strings together.
Strings can be formatted, meaning we can insert variables into strings using placeholders.
Strings can be iterated, meaning we can loop through each character in the string.
Strings can be compared, meaning we can check if two strings are equal or not.
Strings can be searched, meaning we can check if a substring exists in the string.
Strings can be replaced, meaning we can replace a substring with another substring.
Strings can be split, meaning we can break a string into a list of substrings using a delimiter.
Strings can be joined, meaning we can join a list of strings into a single string using a delimiter.
Strings can be stripped, meaning we can remove leading and trailing whitespace from a string.
Strings can be converted to uppercase or lowercase using the upper() and lower() methods.
Strings can be checked for alphanumeric characters using the isalnum() method.
Strings can be checked for alphabetic characters using the isalpha() method.
Strings can be checked for numeric characters using the isnumeric() method.
Strings can be checked for digits using the isdigit() method.
Strings can be checked for whitespace characters using the isspace() method.
Strings can be checked for printable characters using the isprintable() method.
Strings can be checked for title case using the istitle() method.
Strings can be checked for uppercase characters using the isupper() method.
# Strings can be checked for lowercase characters using the islower() method.
# Strings can be checked for capitalized characters using the iscapitalized() method.
# Strings can be checked for punctuation characters using the ispunctuation() method.
'''

Str="Hello World"
print(Str) #Output: Hello World
print(Str[0]) #Output: H
print(Str[1]) #Output: e
print(Str[2]) #Output: l
print(Str[3]) #Output: l
print(Str[4]) #Output: o
print(Str[5]) #Output:

#We can also implement indexing characteristics in strings using loops
name = "Kyojuro Rengoku"
for character in name:
    print(character) #Output: Kyojuro Rengoku
'''
OR
'''
print()
Name = "Sung Jin-Woo"
for i in range(len(Name)):
    print(Name[i]) #Output: Sung Jin-Woo


#Day 12 String slicing and operations

'''
String slicing is the process of extracting a portion of a string using the index.
String slicing is done using the colon (:) operator.
String slicing can be done using the following syntax:
string[start:end:step]
Where:  
start = starting index
end = ending index
step = step size (optional)
'''
#Example of string slicing
fruit="banana"
print(fruit[0:3]) #Output: ban
print(fruit[1:5]) #Output: anan
print(fruit[2:]) #Output: nana
print(fruit[0:6:2]) #Output: bnn
'''
An important point to note is that in string slicing, the starting index is inclusive and the ending index is exclusive. Means when we slice a string, the character at the starting index is included in the sliced string, but the character at the ending index is not included in the sliced string. We can consider it as (n-1) in the sliced string.
'''
#Now lets try out negative indexing/slicing
name="Rengoku"
print(name[-1]) #Output: u
print(name[-6:-1]) #Output: Rengok
print(name[len(name)-6:len(name)-1]) #Output: Rengok, Negative slicing can be understood with the use of len conceptually and can be visualized as forward slicing itself, Which the computer understands by itself.
print(name[-5:-3]) #Output: go
print(name[-1:-6]) #Output: (empty string), Because the first index is smaller than the second index in negative slicing, so it will not return anything.
print(name[-6:-1:-2]) #Output: (empty string), Because the step is negative, but the starting index is less than the ending index, so it will not return anything.
'''
In negative indexing, the last character of the string is at index -1, the second last character is at index -2, and so on. The traversal of the string in case of negative indexing is done from right to left. The last character of the string is at index -1, the second last character is at index -2, and so on. The traversal of the string in case of negative indexing is done from right to left. But the result will be printed in reverse order, i.e from left to right. So a greater index will be printed first and then the smaller index so that negative slicing works and the output is returned in the correct order.
'''