# 1. Identity operators
# Attempt 1,  Using Identity operator, Comparing the price of Petrol and Diesel in Uganda currently using "is" , "is not"
dieselPx = 4890
petrolPx = 5250
paraffinPx = 4550
 
print(dieselPx is petrolPx)  # checking if diesel px is that petrol => False
print(dieselPx is not paraffinPx)  # checking if diesel px is not that paraffin px => True

# 2. Python Logical Operators are used to combine conditional statements:
# Attempt 2, Comparing the price of different commodities on market using logical "and" , "or" , "not"
matooke = 9000
rice = 8000
sugar =5500
print(matooke>5000 and rice>5000 and sugar>6000) # False cause px of sugar<6000 even if other px are true
print(matooke>5000 or rice>5000 or sugar>6000) # True cause px of all True
print(not(matooke > 5000 and rice > 5000) and sugar>5000) # False cause "not" is reversing the result


#3. Python Comparison Operators
# Comparison operators compare variables and return a boolean result: True or False.
# Attempt 3, Here comparing the price of Petrol, paraffin and Diesel in 
#   Uganda currently using ">" , "<" , "!=", "<=" , ">=" , "=="
 
dieselPx = 4890
petrolPx = 5250
paraffinPx = 4550
 
print(dieselPx > petrolPx)  # checking if diesel px is above petrol => False
print(paraffinPx < petrolPx )  # checking if paraffin px is below petrol => True
print(paraffinPx != dieselPx ) # checks if paraffin px is not equal to diesel =>True
print(petrolPx >= paraffinPx ) # checks if petrol px greater or equal to paraffin =>True
print(paraffinPx == petrolPx ) # checks if parrafin px is equal to petrol =>False



