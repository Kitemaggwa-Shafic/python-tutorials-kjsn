# Reserved key word, words with special meaning in programing

# and, assert, break, class, continue, del, if, def, except, final, import, in, is, lambda, raise
# try, else, or, execept, while, for, from, finally, global, not, pass, print, return, exec, elif

# FUNCTIONS
'''
a named group of statements related to one another performing a certain task

Syntax
def functionName():
    Block of code
functionName() # Calling yo function to execute

# predefined functions take in a parameter eg flot, str, print, type etc
# pre-defined functions, are special function already defined in python eg print,
#   
'''

def person():
    pass # read about pass

# function adding two number

def addNumbers():  
    num1, num2 = 5,4
    num3 =  num1 + num2
    print(num3) # this will not print out because the function name hasnt been called
addNumbers() # calling the function name to have the result printed

#creat a function with list of numbers and prints them out
def listNum():
    numberList = [10,20,30,40,50,60,70,80,90,100]
    print(numberList) # end of my function definition, from line 33 to 35
listNum()   #function invocation

def numList():
    numberList = [10,20,30,40,50,60]
    for item in numberList:
        print(item) 
numList() #calling my numList function

# function with no argument
# add_numbers()
    # code


# a Function cheking if numbers in a list are even numbers and odd

def evenFunction():
    numberList = [1,2,3,4,5,6,7,8,9]
    for number in numberList:
        if number % 2 ==0:
            print(number, "Is even number, from our list of 1 to 10")
        else:
            print(number, "odd number in list")
evenFunction()

# Types of functions
# 1. static function is a function with variable values within itsself, like above, the PC knows what to deal with
# 2. Dynamic function is a function with values at function calling, takes in both parameters and values

# Example of dynamic function

# function with two arguments
def add_numbers(num1, num2): # definining a function with paraters here num1, num2
    sum = num1 + num2
    print('Sum of numbers num1 and num2: ',sum)
    
add_numbers(2,3) # 2,3 are arguments which are actual values to parameters (num1, num2) on line 67
add_numbers(12,6)

#
def weight(maize, rice):
    total = maize + rice
    print("the total weight is", total ,"kgs, for both maize and rice")
weight(300, 120) # at function call, parse in the real values to use    

#def
def myNumbers(a):
    for i in range (a):
        print(i)
myNumbers(10) # we are iterating through numbers and range is stopping on 10





# Using the break and continue
'''
1. If you ever need to skip part of the current loop you are in or break out of the loop completely,
then you can use the break and continue statements.
2. You can use the break statement if you need to break out of a for or while loop and move onto the next section of code.
3. The break and continue statements in Python are used to skip parts of the current loop or break out of the loop completely.
4. The break statement can be used if you need to break out of a for or while loop and move onto the next section of code.
5. The continue statement can be used if you need to skip the current iteration of a for or while loop and move onto the next iteration.
'''
# Examples of break
for letter in 'Kite maggwa':
    if letter == "m": # condition to check if letter is "m", will stop,
        break # im instructing that if you reach "m" stop printing letters
    print('letter :', letter)

# using a while loop to increament from 5 to 20
num = 5
while num < 20:
    print('My number :', num)
    num = num + 1
    
# Using the same example to break as long as the number is "9"
num = 5
while num < 20:
    print('Current number :', num)
    num = num + 1
    if num == 9: # condition to check num is "9", as long as it is
        break   # execution will break here at '8'

# Using Continue
# You can use the continue statement if you need to skip the current iteration of a
# for or while loop and move onto the next iteration.

# Example 1
for letters in "Kitiibwa":
      if letters == "i": # condition to check as long as letter is "i", will be skipped, 
        continue            # but because of continue, it will other letters
      print(letters)
# Example using iterations
num = 10
while num < 100:
    num = num + 10
    if num == 50:  # condition to check if '50' is in loop
        continue # will continue from here but now with '60', for '50' is out upto '100'
    print("Current num: ", num)

# Read about pass keyword
'''
Pass: key word
Pass: The pass statement in Python is used when a statement or a condition is required to be present in the program,
but we don’t want any command or code to execute. It’s typically used as a placeholder for future code.#
'''














 
