
class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"{self.name}'s deposit is {self.deposit} and loan is {self.loan}"
    

    def add_deposit(self, amount):
        self.deposit += amount
    

    def add_loan(self, amount):
        self.loan += amount


    def withdraw(self, amount):
        if self.deposit >= amount:
            self.deposit -= amount
        else:
            print("Balance isn't enought. Withdrawal canceled!")

