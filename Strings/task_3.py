'''
task : 6 
Write a Python program to count the number of strings from a given list of strings. 
	The string length is 2 or more and the first and last characters are the same.
	
	Sample List : ['abc', 'xyz', 'aba', '1221']
	Expected Result : 2
'''

Sample_List = ['abc' , 'xyz' , 'aba' , '1221']

length = len(Sample_List)

count = 0

print(Sample_List)

for i in Sample_List :
    if(i[0] == i[-1] and length >= 2) :
        count += 1 # count = count + 1
    
print("\nExpected Result :",count)