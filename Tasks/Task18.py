# finding out that a given post for social media is talking about Chirag or not...

post = input("Enter the Post : ")

if("chirag".upper() in post.upper()) :
    print('Yes,this post can be talking about Chirag...')

else :
    print('No,this post can not be talking about Chirag...')