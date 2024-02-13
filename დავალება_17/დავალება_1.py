# აღწერეთ ორი კლასი შემდეგი მონაცემების მიხედვით:

# Person:
# name:
# deposit (default value = 1000, მიუთითებს ამჟამად რამდენი აქვს დეპოზიტზე)
# loan (default value = 0, მიუთითებს ამჟამად რამდენი აქვს სესხი აღებული)

# House:
# ID – ბინის საკატასტრო კოდი
# price – ბინის ფასი
# owner – სახლის მეპატრონე (Person ტიპის ობიექტი)
# status – ახალი ბინის დამატებისას სტატუსი არის ყოველთვის “გასაყიდი”

# გაითვალისწინეთ owner-ის მნიშვნელობა არის Person კლასის ობიექტი
# Person კლასში დაამატეთ __str__ მეთოდი რომელიც დააბრუნებს პიროვნების სრულ ინფორმაციას
# შექმენით ორი Person კლასის ობიექტი(მაგალითად ერთი მეპატრონე, მეორე მყიდველი). ასევე შექმენით House კლასის
# ობიექტი რომლის owner იქნება ერთ-ერთი Person ობიექტი

# House კლასში დაამატეთ ბინის გაყიდვის მეთოდი, რომლის დროსაც პარამეტრებად გადაეცემა მყიდველი, თუ მეტი
# პარამეტრი არ გადაეცემა, ამ დროს უნდა შესრულდეს ბინის გაყიდვის ოპერაცია(გამყიდველის deposit უნდა გაიზარდოს
# ბინის ღირებულებით, უნდა შეიცვალოს owner და status უნდა გახდეს “გაყიდული”, დაბეჭდეთ შესაბამისი ტექსტი).
# თუ ამ მეთოდის გამოძახების დროს მყიდველის გარდა პარამეტრად გადაეცა კიდევ ერთი რიცხვი, მაშინ შესრულდეს
# ბინის სესხით გაყიდვის ოპერაცია, სადაც პარამეტრად გადაცემული რიცხვი მიუთითებს მყიდველის მიერ აღებული
# სესხის რაოდენობას, მეთოდმა კი უნდა შეასრულოს შემდეგი ოპერაციები: გამყიდველის deposit უნდა გაიზარდოს
# ბინის ღირებულებით, owner უნდა შეიცვალოს, status გახდეს “გაყიდული სესხით”, მყიდველის სესხი (loan) უნდა
# გაიზარდოს შესაბამისი რაოდენობით და დაიბეჭდოს გაყიდვის შესაბამისი შეტყობინება.
# კლასის გარეთ მოახდინეთ აღწერილი ფუნქციების გამოძახება


from person import Person

class House:
    def __init__(self, ID, price, owner, status="For sale"):
        self.id = ID
        self.price = price
        self.owner = owner
        self.status = status

    def __str__(self):
        return f"{self.owner.name} is this house owner. House price is {self.price} and status is {self.status}"
    

    def sold_house(self, customer, loan=0):
        if customer:
            total_balance = customer.deposit + customer.loan
            if total_balance < self.price:
                remaining_loan = self.price - total_balance
                print(f"{customer.name} doesn't have enough funds to purchase this house. {customer.name} needs {remaining_loan} loan for purchase!")
            
                if remaining_loan > loan:
                    return f"{customer.name} has {loan} loan but needs a larger loan to purchase this house."
                else:
                    total_balance = loan - remaining_loan 
                    customer.loan += loan
                    print(f"{customer.name} has additional loan {loan} and it is enought to purchase this house!")
            else:
                total_balance -= self.price
    
            self.owner.deposit += self.price
            print(f"After sold house, {self.owner}")
            self.owner = customer
            self.status = "Sold"
            return f"{self.owner.name} is now the owner of the house. Total Balanse is {total_balance}. House status is {self.status}."
        else:
            return "No customer provided for the transaction."


        
owner = Person("OWNER")
buyer = Person("BUYER")
buyer2 = Person("BUYER2")

buyer2.add_loan(1500)
buyer2.add_deposit(3000)

house = House("12345", 10000, owner)

print(owner)
print(buyer)
print(buyer2)
print(house, "\n")

print(house.sold_house(buyer, 6000), "\n")
print(house,"\n")
print(house.sold_house(buyer2, 8000))


