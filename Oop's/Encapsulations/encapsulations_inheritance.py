# in this python program , we are seeing the combinations of set , get methods(encapsulations) and inheritance...

# using set methods we can be easily modify or change or update the data of the class...

class employee :
    
    # Parameterized Constructors
    def __init__(self , id , name , salary) :

        self.__id = id # Private scope of visibility
        self.__name = name # Private scope of visibility
        self.__salary = salary # Private scope of visibility

    def get_id(self) :
        return self.__id

    def get_name(self) : # Encapsulations getter methods 
        return self.__name

    def get_salary(self) :
        return self.__salary

    def set_name(self , name) : # Encapsulations setter methods
        self.__name = name

    def set_salary(self , salary) :
        self.__salary = salary

    def display_emp(self) :
        print("\nThe Employee ID is :",self.__id)
        print("\nThe Employee Name is :",self.__name)
        print("\nThe Employee Salary is :",self.__salary)

class manager(employee) : # inherites the employee class -- Single Inheritance
    def __init__(self , id , name , salary , department) :
        # super().__init__(id , name , salary)
        employee.__init__(self , id , name , salary)
        self.__department = department

    def get_department(self) :
        return self.__department
    
    def set_department(self , department) :
        self.__department = department

    def display_man(self) :
        employee.display_emp(self)
        print("\nThe Manager Department is :",self.__department)

class developer(employee) : # it will be inherites the employee class base class --- Hierarchical Inheritance
    def __init__(self, id, name, salary , language) :
        super().__init__(id, name, salary)
        self.__language = language

    def get_language(self) :
        return self.__language
    
    def set_language(self , language) :
        self.__language = language

    def display_dev(self) :
        self.display_emp()
        print("\nThe Developer Language is :",self.__language)

class senior_developer(developer) : # it will be inherites the developer class ---> Multiple Inheritance
    def __init__(self, id, name, salary, language , experience) :
        super().__init__(id, name, salary, language)
        self.__experience = experience

    def get_experience(self) :
        return self.__experience
    
    def set_experience(self , experience) :
        self.__experience = experience

    def display_senior_dev(self) :
        # developer.display_dev(self)
        self.display_dev()
        print("\nThe Senior Developer Experience is :",self.__experience)

class bonus :
    def __init__(self , bonus):
        self.__bonus = bonus

    def get_bonus(self) :
        return self.__bonus
    
class tech_lead(developer , bonus) : # it will be inherites the both class of developer and bonus --- Multiple Inheritance
    def __init__(self, id, name, salary, language , bonus):
        super().__init__(id, name, salary, language)
        bonus.__init__(self , bonus)

    def display_tech_lead(self) :
        self.display_dev()
        print("\nThe Tech Lead Bonus is :",self.__bonus)

class hybrid_emp(senior_developer , bonus) : # it will be inherites the class of senior developer and bonus --- Hybrid Inheritance
    def __init__(self, id, name, salary, language, experience , bonus):
        super().__init__(id, name, salary, language, experience)
        bonus.__init__(self , bonus)

    def display_hybridemp(self) :
        self.display_senior_dev()
        print("\nThe Bonus is :",self.__bonus)

# menu driven :-

emp_list = []

def add_employee() :
    emp_id = int(input("\nEnter the Employee ID : "))
    emp_name = input("\nEnter the Employee Name : ")
    emp_salary = int(input("\nEnter the Employee Salary : "))

    emp = employee(emp_id , emp_name , emp_salary)

    emp_list.append(emp)

    print("\nEmployee Added Successfully!!")

def display_employee() :
    if not emp_list :
        print("\nNo Employee Added...")
    else :
        for emp in emp_list :
            emp.display_emp()

def update_employee() :
    id = int(input("\nEnter the ID that you want to be update : "))

    for emp in emp_list :
        if id == emp.get_id() :
            name = input("\nEnter the Updated Name : ")
            salary = int(input("\nEnter the Updated Salary : "))

            if name :
                emp.set_name(name)

            if salary :
                emp.set_salary(salary)

            print("\nEmployee Updated Successfully!!")    
            return
         
    print("\nInvalid ID...")

def delete_employee() :
    id = int(input("\nEnter the ID that you want to be Delete : "))

    for emp in emp_list :
        if id == emp.get_id() :
            emp_list.remove(emp)

            print("\nEmployee Deleted Successfully!!")
            return    
        
    print("\nInvalid ID...")

def main() :
    while True :
        print("\n1. Add Employee")
        print("\n2. Display Employee")
        print("\n3. Update Employee")
        print("\n4. Delete Employee")
        print("\n5. Exit")

        choice = int(input("\nEnter the Choice (1 - 5) : "))

        if(choice == 1) :
            add_employee()

        elif choice == 2 :
            display_employee()

        elif choice == 3 :
            update_employee()

        elif choice == 4 :
            delete_employee()

        elif choice == 5 :
            break

        else :
            print("\nInvalid Choice of Selection!!")

main()