

squared_numbers = tuple((lambda x = i: x ** 2)() for i in range(1, 11))
print(squared_numbers)