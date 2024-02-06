# დავალება 2.

# გამოიყენეთ organizations-100.csv
# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “ssl_companies.csv” და ჩაწერეთ მხოლოდ აიდი, კომპანიის სახელი,
# ვებ საიტი, ინდუსტრია და დასაქმებულების რაოდენობა ისეთი კომპანიების რომელთაც აქვთ ssl-ით დაცული ვებსაიტი(HTTPS)

import csv

with open("organizations-100.csv", "r") as organization_file:
    organization_reader = csv.DictReader(organization_file)
    

    with open("ssl_companies.csv", "w", newline="") as ssl_file:
        headers = ["Organization Id", "Name", "Website", "Industry", "Number of employees"]
        ssl_writer = csv.DictWriter(ssl_file, fieldnames=headers)
        ssl_writer.writeheader()

        for row in organization_reader:
            del row["Index"]
            del row["Country"]
            del row["Description"]
            del row["Founded"]
            
            if 'https' in row["Website"]:
                ssl_writer.writerow(row)
        
