def factorial(num):
    if num <= 1 :
        return 1
    else:
        return num * factorial(num - 1)
  
    
input_num = int(input("Enter number: "))
print(factorial(input_num))