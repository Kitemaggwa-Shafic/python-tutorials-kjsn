# Python data types
'''
=> Data types telling the computer the kind of data it will store in the memory space
=> Are used to optmise the physcial storage of our memory space
=> Logical categories of data that the computer is dealing with, storing or processing in its memory  '''
# int a = 4  (creating a variable a of interger data type and assigning it 4 (other languages))
# in python it changes, it can be able to know the kind of data type with it
# Examples of datatypes
'''
1. int => an integer whole number
2. string => a group of characters in quotes
3. list   => variable that stores more than one value at once and in "[]" ie [1,2,3] and can be changed accssed using position values
            either left to right or left to right
4. float  => value with dps
5. complex  => value which are not normal number like mtc formulaes
        (floats, int, complex are numerical data types)
6. tuple    => variable that stores more than one value at once and in "()" ie (1,2,3) and can't be changed
7. dict  => variable storing key value pair
8. set   => stores values minus repeating them, removes duplicates from data data listed
'''

# 1. Int data type
age = 18        # denotes an int data type

# 2. String data type
firstName = "Kitemaggwa"    # denotes a string data type

print(type(age)) # asking python which datatype this is => <class 'int'> for integer
print(type(firstName)) # asking python which datatype this is => <class 'str'> for string
# <class 'str'> uses this because python takes all values to be a thing, over roll type of data is class which
# belong to an object, making Object Oriented programming (OOP)
number5 = "120"
print(type(number5)) # asking python which datatype this is => <class 'str'> for string, for strings are inside "",however much we have a number

# How do we store more than one value in the same memory space, separately, we use a list of values
# 'LIST' variable that stores more than one value.
# A list is mutable, which suggests we will modify the list ie( you can add & remove anything in the list)

# 3. List data type
ourNames =["Shafic", "Audrie", "Fabio"]         # denotes a list data type
# three values stored in one variable name, but we always start them from 0,1,2...
# if i want to access Shafic from the list of name above,
print(ourNames[0]) # Telling python to to the list and select name in position 1 ie Shafic
print(ourNames[2]) # Telling python to to the list and select name in position 1 ie Fabio

print(type(ourNames)) # asking python which datatype this is => <class 'list'> list, cause the name variable has more than one
                # variable assigned to it at once

# Data types continued, Day 6

# 4. Float Data type
volume = 23.5
print(type(volume)) # for data type => float

# 5. Complex data type
num1 = 1 + 2j
print(type(num1)) # for data type => complex

# Index values in lists, looking at how to access values stored inside them
numbers = [1,2,3,4,5,6]
names = ['Ozzy', 'Mariam', 'Shafic']
number_names = [[1,2,3,4,5,6],['Ozzy', 'Mariam', 'Shafic']]
print(numbers[0])   # indexing numbers from left to right, we start from 0,1,2... : (Result => 1)
print(numbers[5])
print(numbers[-1])  # indexing numbers from right to left, we start from -1, -2... : (Result => 6)
print(number_names[0][-1]) # will print 6, go to index 0 (of number_names), move backward (-1)
print(number_names[1][-1]) # will print shafic, go to index 1 (of number_names) move backward (-1)

# 6. Tuple Data type
cars = ('Alteza', 'Subaru', 'Ipsum', 'Benz') # tuple, we access the values in it like how do in lists,
# a tuple is immutable ie
# (when you create it you can't add & remove from to it or these values are readonly, you just access them)
print(type(cars)) ## for data type => tuple 
print(cars[2]) # ipsum, we look at their results like we in lists

# 7. Dict Data type
# 
person = {'name':'Tyna','age':'20','height':'170','gender':'female'} # storing them in key:valuepair
print(person['name']) # listing the value corresponding to "name" : (result=> Tyna)
print(type(person)) # for data type => dict for dictionary => <class 'dict'>
print(person.keys()) # looking at keys in the dict => (['name','age','height','gender'])
print(person.values()) # looking at the values of the keys => (['Tyna','20','170','female'])

# 8. Set Data type
oranges = {10, 20, 30, 40, 50, 20, 40, 70}
print(oranges) # stores values minus repeating them, removes duplicates from data data listed

'''
Type Casting: chaging the data type of  a variable to another data type of your choice
'''

myNumber = 20
print(float(myNumber)) # changes the variable to a float however much it was an int
print(str(myNumber))    # changes the variable to a string however much it was an int
print(complex(myNumber)) # changes the variable to a complex number however much it was an int
print(bin(myNumber)) # changes the variable to a binary number however much it was an int





