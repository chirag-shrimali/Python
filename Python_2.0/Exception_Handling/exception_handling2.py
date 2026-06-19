try :

    no1 = int(input("\nEnter the No1 : "))

    no2 = int(input("\nEnter the No2 : "))

    ans = no1 / no2

    print(ans)

except ZeroDivisionError as z :

    print("DivisionError..." , z)

except ValueError as v :

    print("ValueError..." , v)

except :

    print("Error")

finally :

    print("The Code is Terminated...")