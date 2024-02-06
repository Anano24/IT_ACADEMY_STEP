import random

my_list = []

for i in range(10):
    my_list.append(random.randint(10, 30))

print(min(my_list))
print(max(my_list))
