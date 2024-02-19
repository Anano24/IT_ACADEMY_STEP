# დავალება 3.

# დაწერეთ ტრანზაქციის ფუნქცია, რომელსაც გადაეცემა ატრიბუტად ბალანსი და გადასახდელი თანხა,
# დაუწერეთ დეკორატორი, რომელიც საკომისიოს ჩამოაჭრის 1 ლარს და თუ საკმარისი თანხა არ იქნება ანგარიშზე
# დაუბრუნეთ შეცდომის ტექსტი


def decorator(func):
    def wrapper(balance, amount):
        if balance < amount:
            return f"balance is not enought!"
        else:
            balance -= amount
            func(balance, amount)
        return f"after transaction balance is {balance}"
    
    return wrapper



@decorator
def transaction(balance, amount):
    return balance, amount


try:
    result = transaction(10, 1)
    print(result)
except TypeError as e:
    print(e)

