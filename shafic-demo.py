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
'''
####
###
##
# Simple and better Grade compiler in python
# Calculate grade based on average marks in 5 subjects
print("\n")
print("=================================================")
print("|| KIKANDWA   STUDENTS    GRADING    SYSTEM    ||")
print("=================================================")
firstName = (input("Enter First Name : " ) )
lastName = (input("Enter Last Name : " ))
stdClass = str(input("Enter Class : " ))
english   = int(input("Enter English Marks : "))
maths     = int(input("Enter  Maths Marks : "))
physics   = int(input("Enter Physics Marks : "))
chemistry  = int(input("Enter Chemistry Marks : "))
biology    = int(input("Enter Biology Marks : "))
history    = int(input("Enter History Marks : "))
luganda    = int(input("Enter Luganda Marks : "))
geog    = int(input("Enter Geography Marks : "))
comm = int(input("Enter Commerce Marks : "))
comp  = int(input("Enter Computer Marks : "))
lit = int(input("Enter Literature Marks : "))
fineArt = int(input("Enter Fine Art Marks : "))


totalMarks = english + maths + physics + chemistry  + biology + history + luganda + geog + comm + comp + lit + fineArt
average = round((totalMarks / 12),0)

print("-----------------------------")
print("NAME OF STUDENT : ",firstName, lastName, stdClass)
print("-----------------------------")
print("SUBJECT             ", "|MARKS   ", "|GRADE")
print("-----------------------------")
print("ENGLISH:             |", english , "%","|" )
print("MATHEMATICS :        |", maths ,   "%","|")
print("PHYSICS :            |", physics,  "%","|")
print("CHEMISTRY :          |", chemistry,"%","|")
print("BIOLOGY :            |", biology,  "%","|")
print("HISTORY :            |", history,  "%","|")
print("GEOGRAPHY :          |", geog,     "%","|")
print("COMMERCE :           |", comm ,    "%","|")
print("COMPUTER :           |", comp,     "%","|")
print("LITERATURE :         |", lit,      "%","|")
print("FINE ART :           |", fineArt,  "%","|")
print("_____________________________")
print("Total Marks scored :  ", totalMarks)
print("---------------------------- ")
print("Average scored :    ", average,"%")

if average >= 91 and average <= 100:
    print("Your Grade is D1")
elif average >= 81 and average < 91:
    print("Your Grade is D2")
elif average >= 71 and average < 81:
    print("Your Grade is C3")
elif average >= 61 and average < 71:
    print("Your Grade is C4")
elif average >= 51 and average < 61:
    print("Your Grade is C5")
elif average >= 41 and average < 51:
    print("Your Grade is C6")
elif average >= 33 and average < 41:
    print("Your Grade is P7")
elif average >= 25 and average < 33:
    print("Your Grade is P8")
else:
    print(firstName, lastName ,"","F9 and Fail")


