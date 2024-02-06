
def string_ending(string_list, ending):
    try:
        filtered_strings = list(filter(lambda x: x.endswith(ending), string_list))

        if filtered_strings:
            return filtered_strings
        else:
            return "This ending is not in the strings!"
    except TypeError as e:
        print(f"{e}")


params = ['hello', 'str', 'coding', 'nod']
print(string_ending(params, 'ing'))