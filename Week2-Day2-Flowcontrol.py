# Flow control Statements
# Control how the PC executes some instructions basing on certain conditions
# using conditions and loops

# If Condition
'''
Syntax of If
If ( EXPRESSION == TRUE ):
     Block of code # group of statement that are relating to perfom a specific task =>executes when the above condition is True 
else:
     Block of code # executes when the above condition is False
'''
# Examples of if
a = 7
b = 0
if (a > b):
    print('a is greater than b')

listNumber = [10,20,30,50]
print(listNumber)
if(55 in listNumber):
    print('30, is in list of Numbers')

refactoryStudents=['Shafic','Patrick','Malik','Pauline']
if('Pauline' in refactoryStudents): # Testing condition either True / False
    print("Pauline is in Refactory Cohort class") # executes cause if condition is True and Pauline is in list
    print("And shes doing Python")
else:
    print("Shes not in this Cohort") # executes ONLY when the if condition is False

# if, elif and else
# used where you have more than one condition and amongst them one may be true
newNumber = 12
if(newNumber > 0): # Test condition either True / False
    print(newNumber, 'is positive Number') #executes as long the number is positive
elif(newNumber == 0):
    print(newNumber, 'is Zero') #executes as long the number is Zero
else:
    print(newNumber, 'is Negative Number') # executes when we have a neg number


# Nested If these are if statements with in an if statement
#

woman=['short','tall','fat','thin']
if('short' in woman):
    if('fat' in woman):
        print('Man is short and fat')
    else:
            print('Man is just tall')
else:
    print('Man is just thin')


# Loops are for, while loops
# doing something continiuosly oriterating through something until certain condition is false
# for A for loop is used for iterating over a sequence
#   (that is either a list, a tuple, a dictionary, a set, or a string).

numbers =  [10,20,30,50]
for item in numbers:
    print(item) # Will print numbers in the list

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#for in string
for x in "Book":
  print(x) # we are instructing PC to print out letters in word "Book" and we are using x to pick those letters
 


for number in range(10):
    print(number, "is in range of", number " to 10") # will  print numbers from 0,1,2..., 9


# Example of indefinite loop
# While while loop we can execute a set of statements as
#   long as a condition is true
 
i = 1
while i < 6:
  print(i)
  i += 1












