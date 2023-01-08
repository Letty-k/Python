# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:07:31 2023

@author: letty
"""

#strings in python are surrounded by either single or double quotation marks
#For multiple line strings use tripple
#example
print("Hello,World")
print('Whats good')
print(''' my name is Letty
          I am 22 years old
          l am a girl''')
 #ASSIGNING A STRING TO A VARIABLE
'''Assigning a string to a variable is done with the variable
 name followed by an equal sign and the string:'''
 
a="Paper"
print(a)

'''Strings are Arrays
Like many other popular programming languages, strings in Python are arrays 
of bytes representing unicode characters.However, Python does not have a 
character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.'''

'''Get the character at position 1 (remember that the first character has the
 position 0):'''

A = "Hello, World!"
print(A[1])

'''Looping Through a String
Since strings are arrays, we can loop through the characters in a string, 
with a for loop.
Example
Loop through the letters in the word "banana":'''

for x in "banana":
  print(x)
'''String Length
To get the length of a string, use the len() function.

Example
The len() function returns the length of a string'''
print(len(A))

'''CHECKING IF A CHARECTOR IS PRESENT IN A STRING USING *IN* KEYWORD
Example
Check if "can" is present in the following text:'''

b = "How can l help you"
print("can" in b)

c = " Can you help with directons to the mall"
if "help" in c:
  print("Yes, 'help' is present.")
  
  '''Check if NOT
To check if a certain phrase or character is NOT present in a string, we
can use the keyword not in.
Example
Check if "there" is NOT present in the following text:'''

d = "you are almost there"
print("there" not in d)


'''Use the IF NOT in an if statement:

Example
print only if "expensive" is NOT present:'''

if "there" not in d:
  print("No, 'there' is NOT present.")
  
  
  
  
  '''SLICING A STRING
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, 
to return a part of the string.The last index position is not included
Example
Get the characters from position 2 to position 5 (not included):'''

e = "Hello, World!"
print(e[2:5])
#Note: The first character has index 0.

#Slice From the Start
#By leaving out the start index, the range will start at the first character:

#Example
#Get the characters from the start to position 5 (not included):


print(e[:5])

#Slice To the End
#By leaving out the end index, the range will go to the end:

#Example
#Get the characters from position 2, and all the way to the end:

print(e[2:])

'''Negative Indexing
Use negative indexes to start the slice from the end of the string:
Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):'''

print(e[-5:-2])

#NODIFYING STRINGS
#Upper Case 
#Example
#The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

#Lower Case the same goes for lowercase
#Example
#The lower() method returns the string in lower case:

a = "HELLO, WorlD!"
print(a.lower())

#Remove Whitespace using the strip() method
'''Whitespace is the space before and/or after the actual text, and very often
 you want to remove this space.

Example
The strip() method removes any whitespace from the beginning or the end:'''

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#Replace String
#Example
#The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
'''The split() method returns a list where the text between the specified separator
 becomes the list items.

Example
The split() method splits the string into substrings if it finds instances of 
the separator:'''

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


#String Concatenation
#To concatenate, or combine, two strings you can use the + operator.

#Example
#Merge variable a with variable b into variable c:

a = "Hello"
b = "  World"
c = a + b
print(c)

'''Example
To add a space between them, add a " ": or just put some space at  the end 
of preevious string'''

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Format
#As we learned in the Python Variables chapter, we cannot combine strings and
#numbers using the concart methode but we use the formate() methode:
'''The format() method takes the passed arguments, formats them, and places them
 in the string where the placeholders {} are:

Example
Use the format() method to insert numbers into strings:'''

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#The format() method takes unlimited number of arguments, and are placed into
# the respective placeholders:

#Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

#Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))




'''Escape Character
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to 
insert.An example of an illegal character is a double quote inside a string
that is surrounded by double quotes:
Example
You will get an error if you use double quotes inside a string that is
 surrounded by double quotes:'''

#txt = "We are the so-called "Vikings" from the north."
#To fix this problem, use the escape character \":

#Example
#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#other examples of escape charecters are below
#\'	Single Quote	
#\\	Backslash	
#\n	New Line	
#\r	Carriage Return	
#\t	Tab	
#\b	Backspace	
#\f	Form Feed	
#\ooo	Octal value	
#\xhh	Hex value
txt = "This will insert one \\ (backslash)."
print(txt)

#python has many other built in string functions 
