# დავალება 3.

# გამოიყენეთ organizations-100.csv
# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “sorted_csv.csv”
# და ჩაწერეთ დასორტირებული ინფორმაცია, დაასორტირეთ თანამშრომელთა რაოდენობის მიხედვით

import csv


with open("organizations-100.csv", "r") as organizations_file:
    organizations_reader = csv.DictReader(organizations_file)

    # Sort the data based on the "Number of employees" field
    sorted_data = sorted(organizations_reader, key=lambda x: int(x["Number of employees"]))


with open("sorted_csv.csv", "w", newline="") as sorted_file:
    headers = ["Index", "Organization Id", "Name", "Website", "Country", "Description", "Founded", "Industry", "Number of employees"]
    sorted_writer = csv.DictWriter(sorted_file, fieldnames=headers)
    sorted_writer.writeheader()
    sorted_writer.writerows(sorted_data)
        
        