"""
task : 1 create a array using np.ones () 5 X 5...

output  : 

[
    [1 1 1 1 1] ,
    
    [1 0 0 0 1] ,
    
    [1 0 9 0 1] ,
    
    [1 0 0 0 1] ,
    
    [1 1 1 1 1]
]
"""

import numpy as np

x = np.ones((5,5) , dtype = "int")

print(x)

print('---------------------------------')

x[1 : 4 , 1 : 4] = 0

x[2 , 2] = 9

print(x)