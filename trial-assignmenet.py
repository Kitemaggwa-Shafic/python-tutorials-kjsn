# Program to demonstrate use of functions for modularity

# Compute employee's net pay


# Function to get the pay rate from user input
def getPayRate():
    payRate = float(input("Enter the rate of pay for the employee: "))
    return payRate


# Function to get the number of hours worked from user input
def getHoursWorked():
    hoursWorked = int(input("Enter the number of hours worked by the employee: "))
    return hoursWorked


# Function to calculate the gross pay given the pay rate and hours worked
def calculateGrossPay(payRate, hoursWorked):
    grossPay = payRate * hoursWorked
    return grossPay


# Function to calculate the net pay given the gross pay
def calculateNetPay(grossPay):
    deductions = grossPay* 0.20         # Deduction for taxes and benefits
    netPay = grossPay - deductions    # Deduction for taxes and 
    return netPay, deductions


# Function to print the pay check with all associated information on it
def printPayCheck(grossPay, netPay, deductions):
    print("Your net pay is:  $",netPay,"\nCalculated as follows:  \n\tGross Pay = $", grossPay, "\n\tDeductions = $", deductions)
    return


# Main program - looks a lot like the pseudocode for the subtasks that need to be executed
def main():
    payRate = getPayRate()
    hoursWorked = getHoursWorked()
    grossPay = calculateGrossPay(payRate, hoursWorked)
    netPay, deductions = calculateNetPay(grossPay)
    printPayCheck(grossPay, netPay, deductions)

