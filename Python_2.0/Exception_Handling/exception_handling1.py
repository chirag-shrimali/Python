try :

    no1 = int(input("\nEnter the No1 : "))

    no2 = int(input("\nEnter the No2 : "))

    ans = no1 / no2

    print(ans)

except ZeroDivisionError as z :

    print("\nNumber can not be Divide by Zero...")

    print(z)

except (ValueError , TypeError) as v :

    # print("\nValue Error...")

    print(v)

except :

    print("\nError...")

finally :

    print("\nFinally Block is Called...")