
# object is an instance of a class overroll template, 
# object is actual student with actual information
# object is when you create like studnt and give him some inforation from class
# object is the actual student reprsented in class

# from Student script, import Student class
from student import Student

student1 = Student("Shafic", 20,"Maths",False, 4.1) # creating a student object
student2 = Student("Kamagu", 33,"SST",True, 4.7) # creating a student object

print(student1.name) # tryingto access information from student class
print(student2.on_sponsor()) # tryingto access information from student class of student2

