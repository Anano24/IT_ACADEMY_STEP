# დავალების შესასრულებლად გამოიყენეთ movies.json

# წაიკითხეთ მოცემული ფაილი და ამავე ფაილში ჩაწერეთ ის ფილმები, რომელთა გამოშვების თარიღიც არის 2000-ზე მეტი
# და ჟანრი არის Crime, ხოლო Crime სიტყვა ჟანრში შეცვალეთ New_Crime-ით. ამავე ფაილში ჩაწერეთ ისეთი ფილმები,
# რომელთა გამოშვების თარიღიც არის 2000-ზე ნაკლები, ჟანრი არის Drama და ჟანრის სახელი ჩაუწერეთ Old_Drama. იმ ფილმებს,
# რომელიც 2000 წელს არის გამოშვებული ჟანრში ჩაუმატეთ New_Century და ეს ფილმებიც ამავე ფაილში ჩაწერეთ.



import json


# Read the JSON file
try:
    with open('movies.json', 'r') as json_file:
        movie_data = json.load(json_file)
except FileNotFoundError:
    print("File not found!")


# Modify the data in memory
for data in movie_data:
    results = data['results']
    for result in results:
        year, month, day = result['release_date'].split('-')
        genres = result['genres']
        if int(year) > 2000 and 'Crime' in genres:
            genres.remove('Crime')
            genres.append('New_Crime')
        elif int(year) < 2000 and 'Drama' in genres:
            genres.remove('Drama')
            genres.append('Old_Drama')
        elif int(year) == 2000:
            genres.append('New_Century')



# Write the modified data back to the file
try:
    with open('movies.json', 'w') as json_file:
        json.dump(movie_data, json_file, indent=4)
    print("Modifications saved successfully.") 
except Exception as e:
    print(f"An error occurred while writing to file: {e}")          
