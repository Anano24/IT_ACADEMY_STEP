
def add_numbers(number):
   
    if number < 10:
        return number
    else:
        return number % 10 + add_numbers(number // 10)
    

num = int(input('Enter number: '))
print(add_numbers(num))





