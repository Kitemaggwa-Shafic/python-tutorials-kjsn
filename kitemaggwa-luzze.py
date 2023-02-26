# Paired Assignment Weekend 24/02/2023
'''
Pair python assignment 24/02/2023:

Using  dynamic functions, demostrate with an interactive program that reads the name of customer,
name of commodity, price, date of buying, staff/cashier name,
price subtract VAT(18%),

print Net sale of product, name of customer, name of cashier, date

# input (name of customer, name of commodity, price, date, cashier name, auto=>VAT(18%), )
# print (net sale, name ofcustomer, nameof cashier, date)

Copyright by 2 members who design this software

Deadline: Monday, before 10am

'''
print('-----HILLARY QUALITY SNACK CENTER DEMO-----')
customerNames = (input("Enter Customer Names     : "))
productName =  (input("Enter Commodity Name     : "))
productPrice = float(input("Enter Price of Commodity : "))
saleDate = (input("Enter Sale Date        : " ))
cashierName = (input("Enter Cashier Name      : " ))
 
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
print(" Product Net Sale : ", netSale())
print("-----------------------------------")
print("All rights reserved: shafic & denis")






