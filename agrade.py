#
firstName = input("Enter First Name: ")
lastName = input("Enter Last Name : ")
english = int(input("Enter English : "))
mtc = int(input("Enter MTC marks : "))
sci = int(input("Enter science marks : "))
sst = int(input("Enter SST marks : "))
courseWork1 = english + mtc + sci + sst
courseWork2 = english + mtc + sci + sst

def courseWork(): 
    finalCourseWork = courseWork1 + courseWork2 / (40)
    avgCourseWork = finalCourseWork 
    return avgCourseWork
courseWork()
def finalExams():
    totalMarks = english + mtc  + sci + sst 
    avgTotalMarks = totalMarks / 60
    finalMarks = courseWork() + avgTotalMarks
    return finalMarks
finalExams()

 
print("You final marks are " ,finalExams())



