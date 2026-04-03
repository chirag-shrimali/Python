"""
data(.........)

return all keys as list ...

data(name = ajay , age = 23)
"""

def data(**kwargs) :

    ch = kwargs.values()

    print(list(ch))

data(name = "Chirag" , age = 19 , marks = 99 , salary = 15000)