from functools import reduce



def multiple_numbers(numbers):
    try:
        if not numbers:
            raise ValueError("Input list is emplty!")
        
        result = reduce(lambda x, y: x * y, numbers)
        return result
    except TypeError as e:
        print(f"Input list contains non-numeric numbers! {e}")


params = [1, 2, 3, 4, 5]
print(multiple_numbers(params))

