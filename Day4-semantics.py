""" Multi line comments
Semantics about Variables in Python
Variable programmed named memory space in a PC, Rules of naming variables
1. Number should never start a name of a variable ie 1numb = 10
2. Never start with a special character ie $num = 50
3. Its not adivsable to start with capital letters ie Num1 = 30
4. Never leave space btn name of variables ie my salary = 1000
5. variables with compound names use underscore ie my_salary = 2000 or
5. (b) use cameral notation or case instead of underscore (mySalary)
6. Always use shorter names ie
7. Always use relatable names ie salary, age, dob
8. 

"""

# This code here adds two numbers together
num1 = 10
num2 = 5
sum = num1+num2
print(sum)

# Declaring all variables at one line
num3, num4 = 20, 15
print(num3 + num4)


''' Operators in Python, is something that tells a computer what to do with an operand
1. An operand is what an operator acts upon ie 20, 15 acted upon by assignment ,
2. num3 and num4 are operands acted upon by +
3. in brief an operand is refered as  value the operator works upon, boda guy operator are symbols and operand values
4. '''

# Assignment Operator = ie used to assign values or operands to variables
# # this is used to identify comments
# , is used to separate joint statements ie num1,num2,num3
# ! Not

# Arithmetic Operators or types in Python
'''
1. Mathematical Operators ie + - * /
2. floor division // # read about floor divion
3. Exponential operato ** ie num1 ** num2
4. Modulus (%) a remender after a division, a small value % big value you remain with small value eg 5%10 is 5
5. Comparison operators ie >, < , == (Equal), != (Not Equal), is, is not, >=, <=

'''
# mathematical and comparison operators 
num3, num4 = 7, 10
print(num3 +  num4)
print(num3 -  num4)
print(num3 *  num4)
print(num3 /  num4)
print(num3 // num4)
print(num3 %  num4)
print(num3 >  num4)
print(num3 <  num4) 
print(num3 == num4)
print(num3 != num4)
print(num3 is num4)
print(num3 is not num4)


# A statement that evaluates to something is called an "Expression"


# Membership operators ie "in" and "Not in"
'''
Membership operators ie IN and Not IN
In Python, "in" and "not in" are the membership operators in a sequence (strings, lists, or tuple, set dictionary)
1. "in" Returns True if it finds a variable in the specified sequence and false otherwise.
    (They are used to test whether a value or variable is found in a sequence)
2. "not in" Returns True if it does not finds a variable in the specified sequence and false otherwise.
'''
name = "Kitemaggwa"
 
print("a" in name) # prints True, b'se "a" is found in variable name
print('s' not in name) # prints True, b'se "s" is not found in variable name

# Python Logical Operators
'''
Logical operators are used to combine conditional statements:
1. "and"    Returns True if both statements are true / both operands True
2. "or"     Returns True if one of the statements is true / one operand True 	  
3. "not"    Reverse the result, returns False if the result is true not  /True if the operand is False and VV
'''

a=5
b=20
print(a and b)  # will print value of b,  if you have a small number and a bigger number, pc will consider bigger number
print(b and a)  # will print value of a,  if you have a big number and a small number, pc will consider small number
print(b or a)   # will print value of b,  if you have a big number or a small number, pc will consider bigger number
print(a or b)   # will print value of a,  if you have a small number or a bigger number, pc will consider small number
# Profic summary: (with "and" it considers last valriable, "or" considers the first variable)
#logical operators of "and" continued

name_1 = "Shafic"
name_2 = "Audrie"
print(name_1 and name_2)









# Example 2, using a list

a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print ("Line 1 - a is available in the given list")
else:
   print ("Line 1 - a is not available in the given list")

if ( b not in list ):
   print ("Line 2 - b is not available in the given list")
else:
   print ("Line 2 - b is available in the given list")

a = 2
if ( a in list ):
   print ("Line 3 - a is available in the given list")
else:
   print ("Line 3 - a is not available in the given list")


# Logical operator ie "and" , "or" , "not"




