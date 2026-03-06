# word = "pythonprogramming" remove vowels

word = "pythonprogramming"

result = {i for i in word if i not in {'a' , 'e' , 'i' , 'o' , 'u'}}

print(result)

# names = ["Alice", "Bob", "Charlie", "David", "Alex"]

# data = {i[0] for i in names}

# print(data)