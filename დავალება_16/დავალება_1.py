# დავალება 1.

# შეიმუშავეთ საბანკო ანგარიშის ძირითადი სისტემა. შექმენით კლასი სახელწოდებით BankAccount,
# ისეთი ატრიბუტებით, როგორიცაა account_number, account_holder და balance.
# აღწერეთ ფულის ჩარიცხვის და გამოტანის მეთოდები. შექმენით რამდენიმე ობიექტი
# და განახორციელეთ რამდენიმე ტრანზაქცია.



class BankAccount:
   
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

   
    def deposit(self, amount):
        self.balance += amount

    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Balance isn't enought. Withdrawal canceled!")
    

    def get_balance(self):
        return self.balance
       


account = BankAccount('1234567', 'John Doe', 100)

print(f"Balance: {account.get_balance()}")
account.deposit(80)
print("Balance after deposit:", account.get_balance()) 

account.withdraw(30)
print("Balance after withdrawal:", account.get_balance())

account.withdraw(200)
print(f"{account.account_holder} has a balance after attempted withdrawal: {account.get_balance()}\n")


account2 = BankAccount('22334455', 'Emily Smith', 1500)
print(f"Balance: {account2.get_balance()}")
account2.deposit(15)
account2.withdraw(300)
print(f"{account2.account_holder} has a balance of {account2.get_balance()}")


