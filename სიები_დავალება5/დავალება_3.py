my_list = [43, "22", 12, 66, 210, ["hi"]]

print(my_list.index(210))
my_list[5].append("hello")
my_list.pop(2)
print(my_list)

my_list_2 = my_list.copy()
my_list_2.clear()
print(my_list, my_list_2)
