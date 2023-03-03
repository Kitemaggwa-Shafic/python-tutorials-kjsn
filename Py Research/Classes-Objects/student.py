# 3:43:56
# Classes and Objects
# classes 

# not all data can be represented usingstrings, boolean, integers
# like person, phone, computer cant cover these
# we can create our own datatypes to store them with us
# class is bacially define yo own datatypes to store yo stuff
#

# want to represent students in school

class Student:
    # define attributes about student class
    # my initialise function, making out what attributes the student can have
    def __init__(self, name, age,subject,is_admitted,gpa):
        self.name = name # the actual object name will = name they provide to me
        self.age = age
        self.subject = subject
        self.is_admitted = is_admitted
        self.gpa = gpa

        # you can define other functions in classes
        # trying to check with studnt gpa

    def on_sponsor(self):
        if self.gpa > 4.5:
            return True
        else:
            return False
  
        
    
        

