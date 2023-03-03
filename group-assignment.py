# Paired Assignment Weekend 24/02/2023
'''
Pair python assignment 24/02/2023:

Using  dynamic functions, demostrate with an interactive program that reads the name of customer,
name of commodity, price, date of buying, staff/cashier name,
price subtract VAT(18%),

print Net sale of product, name of customer, name of cashier, date

Copyright by 2 members who design this

Deadline: Monday, before 10am

'''

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

print("HILLARY QUALITY SNACK CENTER DEMO")
firstName = (input("Enter First Name : "))
lastName =  (input("Enter Last Name : "))
mySalary = int(input("Enter your Salary : "))
def getPayRate():  
    payRate = mySalary 
    return payRate
# Function to get the number of hours worked from user input salary
def getHoursWorked():
    hoursWorked = getPayRate()*2
    return hoursWorked
getHoursWorked()
print(firstName," yo salary is ", getHoursWorked())


'''
# Paired Assignment Weekend 24/02/2023

Pair python assignment 24/02/2023:

Using  dynamic functions, demostrate with an interactive program that reads the name of customer,
name of commodity, price, date of buying, staff/cashier name,
price subtract VAT(18%),

print Net sale of product, name of customer, name of cashier, date

# input (name of customer, name of commodity, price, date, cashier name, auto=>VAT(18%), )
# print (net sale, name ofcustomer, nameof cashier, date)

Copyright by 2 members who design this

Deadline: Monday, before 10am
'''

# Final send Group assignment good

print('-----HILLARY QUALITY SNACK CENTER DEMO-----')
customerNames = (input("Enter Customer Names   : "))
productName =  (input("Enter Product Name     : "))
productPrice = float(input("Enter Price of Product : "))
saleDate = (input("Enter Sale Date      : " ))
cashierName = (input("Enter Cashier Name     : " ))
 
# functions for calsulations
def autoVAT():
    vat = productPrice * (0.18)
    return vat
autoVAT()
def netSale():
    netPrice = productPrice - autoVAT()
    return netPrice
netSale()
print("-----------------------------------")
print(" Customer Name    : ", customerNames) 
print(" Cashier          : ", cashierName)
print(" Date             : ", saleDate)
print(" VAT              : ", autoVAT())
print(" Product Net Sale : ", netSale())
print("-----------------------------------")
print("All rights reserved: shafic & denis")























