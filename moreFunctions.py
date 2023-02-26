# code a group of statements
# group of statements related to one another
# Expression instruction that evaluates to a value or result ie (a = b+c)
# Function, group of statements related to one another performing a specific task eg cooking: peeling,
# functions stay with def (definition of a function)
# static function function with all definition inside it ie arguments dont change
# dynamic function will have dynamic values and are used at function invocakation
# parameters values declared in function eg def add(num1,num2)
#
# 
# block of code, piece of python code executed as a unit,
#


def myFunction():
    num1, num2 = 10,30
    return num2 # computer finds the return statement, it stops to execute
    total = num1+num2
   # print(total)
print(myFunction()) # prints returned value of the function ie 30, cause return has 'num2' = '30'


def student(name, age, gender):
    print(age)
    print(gender)
    return name, gender # here when ever this function is called, it will return only 2 values or 2 values to share from this function  of name, gender
#student('Chris',30,'male') # invoking a function and assigning arguments
print(student('Chris',30,'male'))
