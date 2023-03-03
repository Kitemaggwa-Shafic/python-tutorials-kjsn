
# Addition Function

def add(): # add is a static function
    num1 = 23
    num2 = 12
    answer = num1 + num2
    print(answer) # print 35 only basing on num1 and num2
add() # invoking of the add function so that it can print out the result 35

def add2(num1, num2):  # add2 is a dynamic function, has parameters provided to it
    num3 = num1 + num2
    print(num3)

add2(21,15) #
add2(100,120)

# Subtract Function

def subtract():
    num1 = 55
    num2 = 12
    num3 = num1 - num2
    print(num3)
subtract()


# Using real world example of employees scenario with return

def employeeSalary():
    salary = 2000
    return salary # identifying a value to be returned & shared by another function outside this function ie in paye

def paye():
    paye = employeeSalary() * 0.3  # here this will get the return value of salary(2000) and multiply it by 30%, but we are accessing salary using the function name employeeSalary   
    finalPaye = employeeSalary() - paye
    #print("Final PAYE is",finalPaye)
    return finalPaye    # telling compiler that when we invoke this function, get us only finapPaye calculated ie in nssf() function

paye() # this willl print a computed value, from two functions above ie (employeeSalary() & paye() )but will have it as one combined

# nssf function using all values from employeeSalary(), paye() all together to compute one result.
def nssf():  
    nssf = paye() * 0.11
    finalNssf = paye() - nssf
    print("NSSF",finalNssf)
nssf()    

# An interact way to have a computer and a user
salary = int(input("Please Enter Your Salary: "))
print("Your Salary is: ", salary)
    

    
 















