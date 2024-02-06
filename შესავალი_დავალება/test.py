
my_count = float(input("თქვენი ბიუჯეტი: "))

commision = 1
money = 20

if my_count > 0:
    new_money = money - commision - my_count
    if new_money <= my_count:
        print("Success")
    else:
        print("Fail")




mark = float(input("თქვენი ნიშანი: "))

if mark <= 100 and mark >= 91:
    print("A")
elif mark <= 90 and mark >= 81:
    print("B")
elif mark <= 80 and mark >= 71:
    print("C")
elif mark <= 70 and mark >= 61:
    print("D")
elif mark <= 60 and mark >= 51:
    print("E")
else:
    print("Fail")