
divisible_by_3 = lambda x: x % 3 == 0


def linear_search(list_for_search, lambda_function):
    
    new_lst = []

    for i in range(len(list_for_search)):
        if lambda_function(list_for_search[i]):
            new_lst.append(i)
        
    return new_lst if new_lst else -1



lst = [5, 17, 24, 12, 77, 30]
result = linear_search(lst, divisible_by_3)
print(result)

