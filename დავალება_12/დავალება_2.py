

operators = {
    "+" : lambda x, y: x + y,
    "-" : lambda x, y: x - y,
    "*" : lambda x, y: x * y,
    "/" : lambda x, y: x / y,
    "**" : lambda x, y: x ** y,
    "%" : lambda x, y: x % y,
}


def calculator(operator, num_1, num_2,):
    if operator in operators:
        operation = operators[operator]
        result = operation(num_1, num_2)
        return result
    else:
        return "Invalid operator"


operator = input("Enter the operator (+, -, *, /, %, **): ")
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

result = calculator(operator, number_1, number_2)


print(f'Result: {result}')