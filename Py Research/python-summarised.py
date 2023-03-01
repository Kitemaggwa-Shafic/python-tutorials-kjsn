# in this im trying to look at the different ways how i can work with string
phrase = "Refactory Bootcamp"
'''
# working with other functions of string in python
print(phrase.upper()) # upper() are functions defined in python
print(phrase.upper().isupper()) # combining 2 functions as one
print(len(phrase)) # checking the lenght of string using 'len'
print(phrase[2]) # checking the character at '2' is "f"
print(phrase.index("B")) # checking the index number of "B" is '10'
print(phrase.index("camp")) # checking the index number starting "camp" is at '14'
print(phrase.replace("factory","ICT")) # replaces "factory" with 'ICT'

# working with Numbers in python
print(2.9093)
print(3 + 2.3)
print(3 + (3 * 4))
print(10 % 3)
print(str(5) +  " my school number") # since we cant have numbers & string, we type cast it with "str" and add other strings
print(abs(-5)) # gives the absolute number of "-5" is '5'
print(pow(2,3)) # gives power of "2" but "3x" is '8'
print(max(3,7)) # max of both numbers
print(round(3.7)) # give the round of number "3.7" is '4'
print("----------------------")
# using more math functions
# for us to use them we need to import them from math
from math import * # gives us access to alot other MTc functions
myNum = -5
print(sqrt(36))
print(sin(90))
print("----------------------")
'''

'''
# Getting information from user
myName = input("Enter your name :")
age = input("Enter your age :")
print("Hello " + myName + "! You are " +age)
print("----------------------")
# Basic Calculatr
num1 = input("Enter first Number : ")
num2 = input("Enter second Number : ")
result = int(num1) + int(num2)
print("The sum of number1 and number2 is " ,result) 

# Simple Mad libs Game
print("----------------------")
color = input("Enter Your color :")
noun = input("Enter Noun :")
celebrity = input("Enter Your celebrity :")

print("Roses are " +color)
print(noun+" are blue")
print("I love "+celebrity)

'''

# Lists 
# can contain both numbers and string
friends = ["Isaac", "John", "Tyna", "Sylvie" ,"Audrie"]
print(friends[2]) # accessing friend at index "2" is 'Tyna
print(friends[-3]) # accessing a frind at index "-3" from right is 'John'
print(friends[2:]) # selects  friends from index "2" and above is ["Tyna","Sylvie","Audrie"]
print(friends[1:3]) # selects  fiends at index "1" & "2" and will leave at "3" and is ["John","Tyna"]
friends[2] = "Richard"  # modifying a friend at index[2]
print(friends[2]) # prints news friend at index[2] as "Richard"
print("----------------------")
print("----------------------")

#
myNumbers =[2, 4, 5, 12, 33, 45]
friends = ["Isaac", "John", "Tyna", "Sylvie" ,"Audrie"]
# extend function appends an elemnt into another list
friends.insert(2,"Fabio") # inserts an item at index[2], and pushes other items after
friends.append("Zahara") # append adds another item to the END of list ie will add "Zahara"
friends.extend(myNumbers) # combines both lists as one list "['Isaac', 'John', 'Tyna', 'Sylvie', 'Audrie', 2, 4, 5, 12, 33, 45]"
friends.remove("John") # Removes an item from list
friends.pop() # removes the last element from the list
#friends.clear() # gives a blank list

# More functions on lists
print(friends)
myNumbers.sort() # sorts otems in Asscending order
myNumbers.reverse() # reverses the items in list
friends2 = friends.copy() # This will copy items in 'friends' and have them in 'friends2'
print(friends.index("Sylvie")) # asking for the index of "Sylvie"
#print(friends.count(3)) # gives the total count of items in list
print("----------------------")
print("----------------------")

# Tuples
# data structure storing different values and immutable (you cant change or modify)
 
cordinates = (4, 5)
print(cordinates[1]) # prints value elemnt in tuple at "1"
cordinates = [(4, 5), (3, 5), (89,3)]
print(cordinates[2])

print("----------------------")
print("----------------------")

# Function collection of code performing a certain task
def sayHello():
    print("Hello Fic!")

print("Top Data")  # will print this first, the down to function name "sayHello()"
sayHello() # function ivoking (calling) and prints "Hello Fic"
print("Bottom") # prints this last

# parameter piece of information to give to a function
# 
def sayHi(name, age): # dynamic function with 2 paremeters name,age
    print("Hello " + name +  "you are ", age)

sayHi("Profic ", 35) # proviidng variables to replace our parameters when this function is called
sayHi("KJSN ", "88")
print("----------------------")

# at 1:34:11
# Using Return statements in functions
# are called when we need information back from the function
def squareNumber(num1):
    return num1*num1

result = squareNumber(3)
print(result) # gets the result sqaure of "3"
print("----------------------")


# IF statements help make decisions basing on different conditions
# 
isMale = True  
isTall = False
if isMale and isTall:
    print("Yes, he a tall male guy ")
elif isMale and not(isTall): # using not() function to negate tall boolean value
    print("Hes a short male")
elif not(isMale) and isTall:
    print("You are not male but tall")
else:
    print("You are not male and not tall")

print("----------------------")

# IF and comparisons

def maxNum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print("Yes, Number 1 is greater than others")
        return num1
    elif num2 >= num1 and num2 >= num3:
        print("Yes, Number 2 is greater than others")
        return num2
    else:
        print("Yes, Number 3 is greater than others")
        return num3
print(maxNum(8,19,4))

print("----------------------")


# More Advanced calculator 
# at 2:00:35
'''
num1 = float(input("Enter First Number : "))
operator = input("Enter MTC Sign : ")
num2 = float(input("Enter Second Number : "))
if operator == "+":
    print("Total is ", num1 + num2)
elif operator == "-":
    print("Difference is ", num1 - num2)
elif operator == "/":
    print("Results is", num1 / num2)
elif operator == "*":
    print("Product is ", num1 * num2)
else:
    print("invalid operator")
'''

# at 2:07:16
# Dictionaries structure to store information in key value pair
# Key:value; 

monthConvert = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
        6: "June",
        7: "July"
}
print(monthConvert["Mar"]) # getting the value of key "Mar"
print(monthConvert.get("May")) # checking  name at a give key
print(monthConvert.get("Dec","Not a valid key")) # instead of printing 'none', we pass in a value to print
print(monthConvert[7])
print("----------------------")
print("----------------------")

# at 2:14:13
# While Loops structure to loop through to execute a code multiple times, until
# a given condition is false
'''
while condition:
    block of code
'''

'''
i = 1
while i <= 10: # condition to execute
    print(i) # print of the number in condition testing
    i += 1 # increamenting the number printed above
print("Done withh loop") # print when condition is False

# at 2:20:01
# Guessing game using a while loop, Ifs

secreteWord = "LOVELY"
userGuess = ""
guessCount = 0 # intialising the guess count, will keep track of how many times a user guess the secrete word
guessLimit = 3 # number of times a user can guess
outOfGuess = False # boolean variable for guess chances

userName = input("Enter Your Name : " )
while userGuess != secreteWord and not(outOfGuess): # looping through conditon as long as all 3 conditions are TRUE
    if guessCount < guessLimit: # checking if user still has some guess chance left
        userGuess = input("Enter Your guess : " ) # if above is TRUE, user will have a chance to enter another guess
        guessCount += 1  # incrementing user guess count value
    else: # user is out of limits
        outOfGuess = True
if outOfGuess: # when user is out of guess, out of guess limit
    print(userName, " Ooppppppp, Out of chances, \n\t YOU LOSE!!!!!!!")
else:  # user still had guess limits, counts, but Guessed the correct word   
    print(userName, " Wawoooo, congs, Yes thats the scerete word, YOU WIN!")
print("----------------------")
print("----------------------")

'''

# at 2:32:44
# For Loops, loop for going through a collecction of items eg tuple, lists, strings etc

for letter in "KITEMAGGWA":
    print(letter)
#
friends =["Isaac", "John", "Audrie"]
for friend in friends: # looping through a list of firnds
    print(friend)

for index in range(10):
    print(index) # prints out number from 0 to 9 with out '10'
print("----------------------")
for index in range(3,7):
    print(index) # prints out number from 3 to 6 with out '7'

friends =["Isaac", "John", "Audrie"]
for index in range(5): # looping through a list of firnds
    if index == 0: # checking inside friends list who is at index[1]
        print(friends[index] ,"First Friend") # printing their name and other text
    else:
        print("Not ma friend") # not one included in if tests
print("----------------------")
print("----------------------")
 

# at 2:41:20
# Exponent Function using a for loop

def power_of_number(number, power_of_number): # taking on number to use and its power
    result = 1 # to store the result
    for index in range(power_of_number): #loop through this range ie 0 all along but not including power number
        result = result * number # result * number to power
    return result
print(power_of_number(3, 2))
print("----------------------")
print("----------------------")

# 2:47:14
# 2D lists and nested for loops


print("----------------------")
print("----------------------")

# 2:52:40
# Building a Translator with for loops, if statements

def translator(phrase):
    translation =""
    for letter in phrase:
        if letter.upper() in "AEIOU":
            if letter.islower():
                translation = translation + "g"
            else:
                translation = translation + "G"
        else:
            translation = translation + letter
    return translation
print(translator(input("Enter a word : " )))
print("----------------------")
print("----------------------")

# 3:04:20
# Try Except allo a program try a piece of code and if not you can account for it in except, 
# Help protect a program and run for some long period minus breaking up
# 
try:
    number = int(input("Enter Number : ") )
    print(number) # if a user enters a text will try it here
except: # will hel us catch error exception and print out 'invalid input'
    print("Invalid input")

# at 3:12:42
# Reading files
# getting info from files out side our python file ie html, text ,csd we use the python read
# reading, opening, closing etc
'''
created a file students.tx you can check it out
Shafic - S4
Isaac - S3
Timo - S1
Anna - S6
'''
# r only read infor= from the file
# w write infoto the file
# a append or add newinfo to end of file
# r+ all power too read and write
#  syntax for file open
'''
variable = open("fileName_path","mode_of_file")
'''
student_file = open("C:/Users/dell/Desktop/KJSN Python Lessons/Py Research/students.txt", "r") # i want to read info in students file

for student in student_file.readlines(): # this for loop reads out students in students file
    print(student)

# print(student_file.read()) # Spreads out all the information in a file toread from
# print(student_file.readline()) # reads an individual line in a file  
# print(student_file.readlines()) # reads all lines in a file and displays in a list[] form 
# print(student_file.readlines()[1]) # reads a specific index[1] of infor in file and displays in a list[] form 
# print(student_file.readable()) # checking is a file is readable b'se of "r" in file open() "True or False"
# print(student_file.writable()) # checking is a file is writable b'se of "r" in file open() "True or False"

student_file.close()

#  Writting to files 
# at 3:21:27


# 3:28:13
# Modules in python any external script you wanna use inside another py script
# importing useful data into your python script and use it
# google list of python modules


# 3:43:56
# Classes and Objects
# classes 






