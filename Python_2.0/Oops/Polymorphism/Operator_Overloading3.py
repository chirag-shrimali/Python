class Emp :

    def __init__(self , salary) :
        
        self.salary = salary

    def __eq__(self, value) :

        return self.salary == value.salary
    
    def __gt__(self, other):
        
        return self.salary > other.salary
    
    def __ge__(self, other) :
        
        return self.salary >= other.salary
    
    def __lt__(self, other):
        
        return self.salary < other.salary
    
    def __le__(self, other) :
        
        return self.salary <= other.salary
        
e1 = Emp(6000)

e2 = Emp(6000)

# if e1 == e2 : 

#     print("Both having Same Salary!!")

# else :

#     print("Both having Different Salary!!")

# if e1 > e2 : 

#     print("Employee - 1 Salary is Greater Than Employee - 2!!")

# else :

#     print("Employee - 2 Salary is Greater Than Employee - 1!!")

if e1 >= e2 : 

    print("Employee - 1 Salary is Greater Than or Equals to Employee - 2!!")

else :

    print("Employee - 2 Salary is Greater Than or Equals to Employee - 1!!")