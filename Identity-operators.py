# Python Special operators
# Python language offers some special types of operators like the identity operator and the membership operator.
# They are described below with examples.

# 1. Identity operators
'''
Identity operators are used to compare the objects, not if they are equal,
but if they are actually the same object, with the same memory location:
  => By using identity operators, Python checks if a particular value is of a particular class or type.
      An identity operator is used most commonly to determine the type of data a variable contains.
   =>  These operators compare the left and right operands and check if they are equal,
      the same object, and have the same memory location.
    
In Python, "is" and "is not" are used to check if two values are located on the same part of the memory.
Two variables that are equal does not imply that they are identical.
1. "is" True if the operands are identical (refer to the same object) x is True
    (Returns true if both variables are the same object) ie True if the type on both sides is the same, whereas is not is opposite to it.
2. "is not" True if the operands are not identical (do not refer to the same object) x is not True
    (Returns true if both variables are not the same object) ie (x is not y)

'''

# Attempt 1,  Using Identity operator, Comparing the price of Petrol and Diesel in Uganda currently using "is" , "is not"
diesel = 4890
petrol = 5250
paraffin = 4550
 
print(diesel is petrol)  # check if diesel px is equal to petrol => False
print(diesel is not paraffin)  # check if diesel px is not equal to paraffin px => True

# Python Logical Operators
'''
Logical operators are used to combine conditional statements:
1. "and"    Returns True if both statements are true / both operands True
2. "or"     Returns True if one of the statements is true / one operand True 	  
3. "not"    Reverse the result, returns False if the result is true not  /True if the operand is False and VV

Logical operators are used to check whether an expression is True or False. They are used in decision-making. For example,
'''
# Attempt 2, Comparing the price of different commodities on market using logical "and" , "or" , "not"
matooke = 9000
rice = 8000
sugar =5500
print(matooke>5000 and rice>5000 and sugar>6000) # False cause px of sugar<6000
print(matooke>5000 or rice>5000 or sugar>6000) # True cause px of all True
print(not(matooke > 5000 and rice > 5000) and sugar>5000) # False cause "not" is reversing the result


