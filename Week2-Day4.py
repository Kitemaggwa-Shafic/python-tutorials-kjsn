


# Addition Function

def add(): # add is a static function
    num1 = 23
    num2 = 12
    answer = num1 + num2
    print(answer) # print 35 only basing on num1 and num2

def add2(num1, num2):  # add2 is a dynamic function
    num3 = num1 + num2
    print(num3)

add2(21,15)
add2(100,120)

add()



# Subtract Function

def subtract():
    num1 = 55
    num2 = 12
    num3 = num1 - num2
    print(num3)
    

subtract()


# Using real world example of employees scenario with return

def employeeSalary():
    salary = 500000
    return salary # identifying a value to be shared by another function outside this function ie in paye

def paye():
    paye = employeeSalary() * 0.3  # here this will get the return value at 39 and multiply it by 30%, but we are accessing salary using the function name employeeSalary   
    finalPaye = employeeSalary() - paye
    print(finalPaye)
    return finalPaye

paye() # this willl print a computed value, from two functions above

#
def nssf():  
    nssf = paye() * 0.011
    finalNssf = paye() - nssf
    print("NSSF",finalNssf)
nssf()    

# An interact way to have a computer and a user
salary = int(input("Please Enter Your Salary: "))
print("Your Salary is: ", salary)
    

    
 















