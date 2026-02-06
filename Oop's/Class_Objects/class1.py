# Oop's :- Object Oriented Programming Langauge

# Public Visibility Of Scope :-

# Use of Data Members Functions or Behaviours

# Class Variable Name
#        |
class Employee :
    emp_name = "Chirag" # Data members or Characteristics or Attributes
    emp_salary = 15000
    emp_age = 19
  
    # Create the members Function

    def display(self) :
        print(f"\nEmployee Name : {self.emp_name}")
        print(f"\nEmployee's Salary : {self.emp_salary}")
        print(f"\nEmployee's Age : {self.emp_age}")

# Create the Object

e = Employee()

e.display()

# Due to Public scope of Visibility they can be update the data members

print("\n====================================================================")

e.emp_name = "Dhwani"

e.emp_salary = 1000

e.emp_age = 23

e.display()