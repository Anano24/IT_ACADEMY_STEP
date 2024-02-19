# დავალება 2.

# დაწერეთ პირველი დავალება ფუნქტორის გამოყენებით



class Functor:
    def __call__(self, *args, **kwargs):
        if not args:
            raise ValueError("No arguments provided")
        elif args[0] < 0:
            raise ValueError(f"{args[0]} is a negative number!")
        else:
            return f"{args[0]} is a positive number"


validator = Functor()
result = validator()
print(result)