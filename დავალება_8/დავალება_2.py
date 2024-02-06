
params = [1, 2, 3, 4, 5, 6, 7]

lst = [(lambda x=i: x)() for i in params if i%2]

print(lst)
