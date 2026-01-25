# Write a program to fill in a letter template given below with name and date. 

"""
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|>
'''
"""

letter = '''\nDear <|Name|>,\n 
        You are selected!\n
    for the Competition Quiz\n
        which can be organized\n
    on <|Date|>\n
        Congratulations!!!
         '''

print(letter.replace('<|Name|>' , "Chirag").replace("<|Date|>" , '4th November,2025'))