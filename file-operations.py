# create a txt file on yo desktop or any other path
# Add some 3 line of data into the file


#Example 1 reading from text files
file = open('C:/Users/dell/Desktop/pythonfile.txt', 'r')
# newdata = file.readlines()
# newdata.pop() # this will return an empty list [] cause we read all lines and last line had not data / empty
# print(file.readline(1)) # this will print data in list format and reads only line eg readlines(2), reads 2 lines
# print(file.read()) # Will print only the data in text files
print(file.readline(5))

 
# Example 2
# file = open('pythonfile.txt')

# for line in file:
#      print(line, end='') # end='' so that we dont print out empty spaces

# Example writting to a text file
# scenario, write a dynamic function
# whih accepts input, compute taxation and write the net pay and tax to a text file to print
# after writting the file email it someone
#

# SHAFIC QUESTIONS FOR MARK OUR COACH
# you said, we need JS so we have to be taken through it though?
# Ask Mark about writting in files for phones and names
# How do you use the , as the limit metre on what youre writting
# 

#

# firstname = str(input("Enter First Name : " ))
# with open('C:/Users/dell/Desktop/Refactory.txt', 'w') as file2:
#     file2.write('\n 1.Man Python is becoming kinda tight now days\n')
#     file2.write('2.But its you who chose it men!!\n' )
#     file2.write(firstname)


# Working with excel files     
# with these files we need special packages to manipulate these file
# import xlwt lib from Workbook

import xlwt
from xlwt import Workbook

wb = Workbook() # declaring a variable for the Workbook
sheet1 = wb.add_sheet('Sheet 1') # Adding in a sheet to the Workbook as 'Sheet 1'
sheet1.write(1,0, 'Names') # Adding columns to sheet 1 created

sheet1.write(1,1, 'Age')

sheet1.write(1,2, 'Class')

wb.save("xlwt examples.xls") # saving the excell workbook with a name.xls
 
