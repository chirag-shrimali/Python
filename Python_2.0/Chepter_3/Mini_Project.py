# Emoji Converter :-

message = input("\nEnter Your Message : ")

msg = (((message.replace(":)" , "😊")).replace(":(" , "😕")).replace(":D" , "😀")).replace(";)" , "😉")

# msg = msg.replace(":(" , "😕")

# msg = msg.replace(":D" , "😀")

# msg = msg.replace(";)" , "😉")

print(msg)