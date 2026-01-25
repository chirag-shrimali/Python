age = int(input("Enter Your Valid Age : ")) # Takes the age from the users
 
# if_elif_else ladder types of programms

if age >= 18 : # checking conditions if entering users age is greater than 18 so it will be prints otherwise else conditions statements 
    print('You are Eligible to get a vehicle licence due to your age is above 18...')
# space in the conditions of if_elif_else is known as indenent
elif age < 0 :
    print('Entering Age is not valid Because age is always has some positive numbers so pls enters a valid age numbers...')

else :
    print("You are Not eligible to get a vehicle licence due to your age is below 18...")