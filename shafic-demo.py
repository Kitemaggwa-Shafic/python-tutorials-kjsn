# Simple Employee Salary Computation
''' 
print("SHAFIC DEMO")
firstName = (input("Enter First Name : "))
lastName = str(input("Enter Last Name : "))
mySalary = str(input("Enter your Salary : "))
def employeeSalary():
    salary = 1000
    return salary
def paye():
    paye = employeeSalary()*0.2
    yourPaye = employeeSalary()-paye
    
    return yourPaye 
print(firstName," yo salary is ", paye())
'''

# Simple and better Salary Compiler in python
print("\n")
print("=================================================")
print("|| EMPLOYEE  SALARY   SIMPLE  COMPILER PYTHON  ||")
print("================================================")
print("\t\t EMPLOYEE DETAILS")
firstName = (input("Enter First Name : " ) )
lastName = (input("Enter Last Name : " ))
age = int(input("Enter Age : " ))
basicPay = int(input("Enter Your Salary : "))
print("")

print("\t\t SALARY DETAILED REPORT")
print("============================================") 
#function to calculate housing allowance
housingAllowance = round((0.4*basicPay),2)
grossPay = round((basicPay + housingAllowance),2)
tax = round((grossPay * .30),5)
netPay = round((grossPay - tax),2)
totalPayment = round((housingAllowance+grossPay+tax+netPay),2)
print("NAME OF EMPLOYEE :       ", firstName, lastName)
print("House Allowance is :     ", housingAllowance)
print("Gross Pay is :           ", grossPay)
print("Tax :                    ", tax)
print("Net Pay is :             ", netPay)
print("____________________________________________")
print("Total Payment :          ",totalPayment)
print("____________________________________________")

if (totalPayment < 400000):
    print(lastName, "Your Payment Mode is  CASH")
else:
    print(lastName, "Your Payment Mode is  CHEQUE")

####
###
##
# Simple and better Grade compiler in python
# Calculate grade based on average marks in 5 subjects
print("\n\n") 
englishMark   = int(input("Enter your mark in English : "))
mathsMark     = int(input("Enter your mark in Maths : "))
physicsMark   = int(input("Enter your mark in Physics : "))
chemistryMark = int(input("Enter your mark in Chemistry : "))
biologyMark   = int(input("Enter your mark in Biology : "))

totalMarks = englishMark + mathsMark + physicsMark + chemistryMark + biologyMark
average = totalMarks / 5

if average >= 91 and average <= 100:
    print("Your Grade is A1")
elif average >= 81 and average < 91:
    print("Your Grade is A2")
elif average >= 71 and average < 81:
    print("Your Grade is B1")
elif average >= 61 and average < 71:
    print("Your Grade is B2")
elif average >= 51 and average < 61:
    print("Your Grade is C1")
elif average >= 41 and average < 51:
    print("Your Grade is C2")
elif average >= 33 and average < 41:
    print("Your Grade is D")
else:
    print("Fail")


