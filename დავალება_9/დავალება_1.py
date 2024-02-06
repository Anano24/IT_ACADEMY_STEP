from random import randint


def random_numbers_list():
    number_list = []

    for _ in range(100):
        number = randint(1, 100)
        number_list.append(number)
    return number_list


def sorted_list():
    numbers_list = random_numbers_list()
    sorted_numbers_list_increase = sorted(numbers_list)
    sorted_numbers_list_decrease = sorted(numbers_list, reverse=True)

    return f'Increasing numbers: {sorted_numbers_list_increase}\nDecreasing numbers: {sorted_numbers_list_decrease}'

    
print(sorted_list())
