# task : 1 sort by second element. (using def function ) 

'''
input : a = [[1,2],[0,4],[5,-2]]
output : a = [[5,-2],[1,2],[0,4]]
'''

def second_value(a) :
    return a[1]

a = [[1 , 2] , [0 , 4] , [5 , -2]]

result = sorted(a , key=second_value)

print(result)