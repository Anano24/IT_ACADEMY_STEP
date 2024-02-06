from random import randint


def random_numbers_list():
    number_list = []

    for _ in range(100):
        number = randint(1, 100)
        number_list.append(number)
    return number_list


def bubbleSort():
    nums_list = random_numbers_list()
    length = len(nums_list)

    for i in range(length):
        swapped = False
        for j in range(length - 1):
            if nums_list[j] > nums_list[j + 1]:
                nums_list[j], nums_list[j + 1] = nums_list[j + 1], nums_list[j]
                swapped = True

        if swapped == False:
            return nums_list


print(f'Increasing numbers by bubble sort algorithm: {bubbleSort()}')



def quickSort(nums):
    length = len(nums)

    if length <= 1:
        return nums
    else:
        pivot = nums.pop()

    greater_nums = []
    lower_nums = []

    for number in nums:
        if number < pivot:
            greater_nums.append(number)
        else:
            lower_nums.append(number)
    return quickSort(lower_nums) + [pivot] + quickSort(greater_nums)


nums_list = random_numbers_list()
sorted_list = quickSort(nums_list)
print("Original list:", nums_list)
print("Sorted list by quick sort algorithm:", sorted_list)