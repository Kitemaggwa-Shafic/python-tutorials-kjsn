# Assignment 
def customer(name, age, loc, sal):
    print("Welcome: " , name)
    print("Your location is: ", loc)
    print("Your Salary : " )
    return sal
name = input("Please Enter Your Name: ")
age = int(input("Please Enter Your Age: "))
loc = input("Please Enter Your Location: ")
sal = float(input("Please Enter Your Salary: "))

def paye(rate):
    customerSalary = customer(name, age, loc, sal)
    customerRate = customerSalary * (rate/100) 
    netSalary = customerSalary - customerRate
    print("Your Final Paye : ", netSalary)

rate = float(input("Please enter your tax rate : "))
paye(rate)

# a function that ivokes another function ic called a calling function



 