# 1. Python Logical Operators are used to combine conditional statements
# Attempt 1, Comparing the repair price of different computers on market using logical "and" , "or" , "not"

dell = 90000
hp = 80000
toshiba = 50000

print(dell>50000 and hp>50000 and toshiba>60000) # False cause px of toshiba<60000 even if other px are true
print(dell>50000 or hp>50000 or toshiba>60000) # True cause px of first True only toshiba
print(not(dell > 50000 and hp > 50000 and toshiba>60000)) # True cause "not" is reversing the result



# 2. Python Comparison Operators
# Comparison operators compare variables and return a boolean result: True or False.
# Attempt 2, Here comparing the price of Petrol, paraffin and Diesel in Uganda currently using ">" , "<" , "!=", "<=" , ">=" , "=="
 
dieselPx = 4890
petrolPx = 5250
paraffinPx = 4550
 
print(dieselPx > petrolPx)     # checking if diesel px is above petrol => False
print(paraffinPx < petrolPx )  # checking if paraffin px is below petrol => True
print(paraffinPx != dieselPx ) # checks if paraffin px is not equal to diesel =>True
print(petrolPx >= paraffinPx ) # checks if petrol px greater or equal to paraffin =>True
print(paraffinPx == petrolPx ) # checks if parrafin px is equal to petrol =>False



# 3. Identity operators
# Attempt 3,  Using Identity operator, comparing the price of Petrol and Diesel in Uganda currently using "is" , "is not"
dieselPx = 4890
petrolPx = 5250
paraffinPx = 4550
 
print(dieselPx is petrolPx)  # checking if diesel px is that petrol => False
print(dieselPx is not paraffinPx)  # checking if diesel px is not that paraffin px => True

