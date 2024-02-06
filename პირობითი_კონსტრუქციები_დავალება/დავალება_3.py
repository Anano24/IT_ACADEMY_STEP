
number_1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
number_2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
operator = input("აირჩიეთ ოპერატორი: '+', '-', '/', '*'\n")

if operator == '+':
    sum = number_1 + number_2
    print(f'ჯამი: {sum}')
elif operator == '-':
    sub = number_1 - number_2
    print(f'სხვაობა: {sub}')
elif operator == '/':
    div = number_1 / number_2
    print(f'განაყოფი: {div}')
elif operator == '*':
    mul = number_1 * number_2
    print(f'ნამრავლი: {mul}')
else:
    print("შეიყვანეთ სწორი მათემატიკური ოპერატორი")
