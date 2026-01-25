# A spam comment is defined by this text containing to detect these spams...

c1 = "Make a lot of money"
c2 = "buy now"
c3 = "subscribe this"
c4 = "click this"

message = input("Enter Your Message : ")

if((c1.lower() in message.lower()) or (c2.lower() in message.lower()) or (c3.lower() in message.lower()) or (c4.lower() in message.lower())) :
    print("This is a seem to be a spam comment...")

else :
    print("This is not a seem to be a spam comment...")