
def func(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)
    combined_tuple = set1.union(set2)
    dublicated_values = set1.intersection(set2)
    return f'Combined: {tuple(combined_tuple)}\nDublicated: {list(dublicated_values)}'


tuple1 = (1,2,3,4,5,6)
tuple2 = (4,5,5,6,6,7)

print(func(tuple1, tuple2))