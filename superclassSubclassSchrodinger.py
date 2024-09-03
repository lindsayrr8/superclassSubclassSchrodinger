
# This program implements a superclass (Person) with two subclasses;
# --- Student, &
# --- Instructor;
# -
# Person has two attributes:
# --- name
# --- birthYear;
# -
# Student has:
# --- major;
# -
# Instructor has:
# --- salary




# Creates parent class Person.
class Person:
    
    def __init__(self, name, birthYear): # Person attributes.
        self.name = name
        self.birthYear = birthYear

    def __str__(self):
        return f"{self.name}, born in {self.birthYear}"


# Creates Student class which inherits from Person.
class Student(Person):
    
    def __init__(self, name, birthYear, major): # Student attributes and inheritable Person attributes.
        super().__init__(name, birthYear)
        self.major = major # Student only attribute.

    def __str__(self):
        return f"Student: {super().__str__()}, majoring in {self.major}"


# Creates Instructor class which inherits from Person.
class Instructor(Person):
    
    def __init__(self, name, birthYear, salary): # Instructor attributes and inheritable Person attributes.
        super().__init__(name, birthYear)
        self.salary = salary # Instructor only attribute.

    def __str__(self):
        return f"Instructor: {super().__str__()}, Salary: ${self.salary}"




# Testing the classes.
def testClasses():
    student = Student("Kat", 1997, "Information Systems")
    instructor = Instructor("Schrödinger", 1979, 64000)

    print(student)
    print(instructor)




testClasses()



