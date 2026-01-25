"""
input : a = [[1 , 2] , [0 , 4] , [5 , -2]]

output : a = [[5 , -2] , [1 , 2] , [0 , 4]]
"""

a = [[1 , 2] , [0 , 4] , [5 , -2]]

x = sorted(a , key=lambda x : x[1])

print(x)