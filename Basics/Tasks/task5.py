# What will be the output of the following snippet of python code?

"""
    print(type(1))  --> <class 'int'>
    print(type(str(True) + '1'))  --> <class 'str'>
    print(type(float(int(0.1))))  --> <class 'float'>
    print(type(True))  --> <class 'bool'>
    print(type(Float(1)))  --> error defined becuse there is float no Float

Answer :-
a.
    int 
    str 
    float 
    bool 
    Error
"""

print(type(1))  # int
print(type(str(True) + '1')) # str  
print(type(float(int(0.1)))) # float
print(type(True))  # bool
print(type(float(1))) # float