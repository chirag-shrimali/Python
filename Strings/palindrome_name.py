name = input("\nEnter the String : ")

if(name[::-1].lower() == name.lower()) :
    print(name,"is a Palindrome String...")
else :
    print(name,'is not a Palindrome String...')