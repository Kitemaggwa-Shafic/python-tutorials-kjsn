# An interactive program of computer and user

name = 'Kitemaggwa'
# input function prompts user for some value from the keyboard, and takes any value as a string
# there4 we have to type cast when reading numeric values from input
age = input("Please Enter Your Age :")
print("The value you have ennter is :", age )
print("-----------")
print("Do you want to continue ?")



# Simple iteraction btn ATM machine and person

languages = ["Luganda","English","Swahili"]
pins = ['123', '456']
transactions = ['withdraw', 'deposit', 'Balance']
a = input("please select your language :")
if(a in languages):
    print("you have selected :", a)
    print("-------------")
    pin =(input("Please enter your pin :"))
    if(pin in pins):
       # print("Yes correct pin, thanks, please continue")
       # print("-------------")
        print("Select your transaction")
else:
    print("Know languages are; Luganda, English, Swahili, please repeat again")
    a = input("please select your language :")

# input function prompts user for some value from the keyboard, and takes any value as a string
# there4 we have to type cast when reading numeric values from input

num1 = input("Enter the price of matooke")
print("the price of matooke is :",num1)
print(type(num1)) # will show that the price is of type String
num2 = int(input("The price of matooke"))
print('The price of matooke is ',num2)
print(type(num2)) # will show that the price is of type int because of type casting

# Paired Assignment Weekend 24/02/2023
'''
Pair python assignment 24/02/2023:

Using  dynamic functions, demostrate with an interactive program that reads the name of customer,
name of commodity, price, date of buying, staff/cashier name,
price subtract VAT(18%) => ,

print Net sale of product, name of customer, name of cashier, date

Copyright by 2 members who design this

Deadline: Monday, before 10am

'''



















