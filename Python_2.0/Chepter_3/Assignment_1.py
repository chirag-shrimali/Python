# Write a Program that takes a sentence and prints :-

'''
1. Total Characters (len())
2. Upper Case Version
3. Lower Case Version
'''

sentence = input("\nEnter Your Sentence : ")

total_ch = len(sentence)

upp_case = sentence.upper()

low_case = sentence.lower()

print("\nTotal Characters :",total_ch)

print("\nUpper Case :",upp_case)

print("\nLower Case :",low_case)