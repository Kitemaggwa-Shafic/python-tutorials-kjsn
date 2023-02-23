# Python data types
'''
=> Data types telling the computer the kind of data it will store in the memory space
=> Are used to optmise the physcial storage of our memory space
=> Logical categories of data that the computer is dealing with, storing or processing in its memory  '''
# int a = 4  (creating a variable a of interger data type and assigning it 4 (other languages))
# in python it changes, it can be able to know the kind of data type with it
# Examples of datatypes

age = 18
firstName = "Kitemaggwa"

print(type(age)) # asking python which datatype this is => <class 'int'> for integer
print(type(firstName)) # asking python which datatype this is => <class 'str'> for string
# <class 'str'> uses this because python takes all values to be a thing, over roll type of data is class which
# belong to an object, making Object Oriented programming (OOP)
number5 = "120"
print(type(number5)) # asking python which datatype this is => <class 'str'> for string, for strings are inside "",however much we have a number

# How do we store more than one value in the same memory space, separately, we use a list of values
# 'LIST' variable that stores more than one value.

name =["Shafic", "Audrie", "Fabio"] # 3 values stored in one variable name, but we always start them from 0,1,2...
# if i want to access Shafic from the list of name above,
print(name[0]) # Telling python to to the list and select name in position 1 ie Shafic
print(name[2]) # Telling python to to the list and select name in position 1 ie Fabio

print(type(name)) # asking python which datatype this is => <class 'list'> list, cause the name variable has more than one
                  # variable assigned to it at once






