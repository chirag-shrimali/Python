# Write the python program of EMPLOYEE MANAGEMENT SYSTEM

print("\n\t\t\t\t\t\t\t|                                  |")
print("\t\t\t\t\t\t\t|----------------------------------|")
print("\t\t\t\t\t\t\t|   EMPLOYEE MANAGEMENT SYSTEM     |")
print("\t\t\t\t\t\t\t|----------------------------------|")
print("\t\t\t\t\t\t\t|                                  |\n\n")

d1 = {}

def add_emp() :
    emp_id = int(input("\nEnter the Employee's ID : "))
    emp_name = input("\nEnter the Employee's Name : ")
    emp_age = int(input("\nEnter the Employee's Age : "))
    emp_salary = int(input("\nEnter the Employee's Salary : "))
    
    d1[emp_id] = {emp_name , emp_age , emp_salary}

    print("\nEmployee Added Successfully!!")

def update_emp() :
    update_emp = int(input("\nEnter the ID that you want to be updated : "))

    if update_emp in d1 :
        update_name = input("\nEnter the Updated Employee Name : ")
        update_age = int(input("\nEnter the Updated Employee Age : "))
        update_salary = int(input("\nEnter the Updated Employee Salary : "))
        d1[update_emp] = {update_name , update_age , update_salary}
        print("\nEmployee Updated Successfully!!")
    else :
        print("\nThe Employee Records are not Found...")

def delete_emp() :
    delete_emp = int(input("\nEnter the ID that you want to be Delete : "))

    if delete_emp in d1 :
        del d1[delete_emp]
        print("\nEmployee Deleted Successfully!!")
    else :
        print("\nThe Employee Records are not Found...")

def search_emp() :
    search_emp = int(input("\nEnter the ID of the employee that you want to be search : "))

    if search_emp in d1 :
        print(d1[search_emp])
    else :
        print("\nThe Searched Employee not found...")

def display_emp() :
    
    for i in d1 :
        print(d1[i])

while True :

        print("1. Add Employee")
        print("\n2. Update Employee")
        print("\n3. Delete Employee")
        print("\n4. Search Employee")
        print("\n5. Display Employee")
        print("\n6. Exit")

        choice = int(input("\nEnter Your Choice (1-6) : "))

        if choice > 0 and choice < 7 :    
        
          match(choice) :

            case 1: add_emp()
        
            case 2: update_emp()
    
            case 3: delete_emp()

            case 4: search_emp()

            case 5: display_emp()

            case 6:
                print("\nExiting Successfully!!")
                break
        else :
            print("\nInvalid Choice Of Selection!!!")
            