# დავალება 1.

# გამოიყენეთ titanic.csv წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი
# csv ფაილი “survived.csv” და ჩაწერეთ მხოლოდ გადარჩენილების ინფორმაცია.


import csv


with open("titanic.csv", "r") as titanic_file:
    titanic_reader = csv.DictReader(titanic_file)
    survived_data = [row for row in titanic_reader if row['Survived'] == '1']


with open("survived.csv", "w", newline="") as survived_file:
    headers = ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]
    survived_writer = csv.DictWriter(survived_file, fieldnames=headers)
    survived_writer.writeheader() 
   
    survived_writer.writerows(survived_data)
                

            