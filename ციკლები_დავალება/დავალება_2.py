total_sum = 0

while True:
    num = int(input("შეიყვანეთ რიცხვი: "))
    if num > 0:
        total_sum += num
    else:
        print("შეიყვანეთ დადებითი რიცხვი!")

    answer = input(
        "დაჯამებისთვის შეიყვანეთ სიტყვა 'sum' ან გასაგრძელებლად დააჭირეთ ენთერს! "
    ).lower()
    if answer == "sum":
        print(f"ჯამი არის: {total_sum}")
        break
