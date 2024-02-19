# დავალება 1.

# დაწერეთ ფუნქცია, რომელიც უბრალოდ აბრუნებს არგუმენტად გადაწოდებულ რიცხვს,
# დაუწერეთ დეკორატორი, რომელიც შეამოწმებს, რომ რიცხვი უნდა იყოს დადებითი,
# თუ არის უარყოფითი ამ შემთხვევაში დააბრუნეთ ValueError შესაბამისი ტექსტით,
# სხვა შემთხვევაში აამოქმედეთ ფუნქცია, შედეგი კი დაბეჭდეთ დეკორატორიდან.



def positive_number(func):
    def wrapper(x):
        if x < 0:
            raise ValueError(f"{x} is a negative number!")
        result = func(x)
        print(f"{x} is a positive number")
        return result

    return wrapper


@positive_number
def number(n):
    return n

print(number(5))