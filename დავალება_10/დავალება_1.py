from random import randint


def random_numbers_list():
    number_list = []

    for _ in range(100):
        number = randint(1, 100)
        number_list.append(number)
    return number_list


def linear_search(list_for_search, value):
    for i in range(len(list_for_search)):
        if list_for_search[i] == value:
            return i
        
    return -1



def quickSort(nums):
    length = len(nums)

    if length <= 1:
        return nums
    else:
        pivot = nums.pop()

    greater_nums = []
    lower_nums = []

    for number in nums:
        if number > pivot:
            greater_nums.append(number)
        else:
            lower_nums.append(number)
    return quickSort(lower_nums) + [pivot] + quickSort(greater_nums)



def binary_search(lst_for_search, value):
    low = 0
    hight = len(lst_for_search)-1
    mid = 0

    while low <= hight:
        mid = (low + hight) // 2

        if lst_for_search[mid] > value:
            hight = mid - 1
        elif lst_for_search[mid] < value:
            low = mid + 1
        else:
            return mid
        
    return -1



random_list = random_numbers_list()
value = 30
print(random_list)
print(f'ხაზობრივი ძიების შედგი არის : {linear_search(random_list, value)}')

sorted_lst = quickSort(random_list)
value_for_search = 25
print(f'სორტირებული სია: {sorted_lst}')
print(f'ორობითი ძებნის შედეგი: {binary_search(sorted_lst, value_for_search)}')

