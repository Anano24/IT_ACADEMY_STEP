# დავალება 1.

# შექმენით რამდენიმე json ფაილი, დაწერეთ მოცემული json ფაილების პარსინგი რომელიც ფაილის სახელთან ერთად
# დაბეჭდავს json-ში არსებულ მონაცემებს და თითოეული ფაილისთვის გაუშვით ცალცალკე ნაკადი(thread)



import json
import threading
from faker import Faker


fake = Faker()

# Function to create JSON files with fake data
def make_jsons(file_path):
    data_list = []

    for _ in range(10):
        data = {'name': fake.name(), 'country': fake.country()}
        data_list.append(data)

    # Write data to the JSON file
    with open(file_path, 'w') as file:
        json.dump(data_list, file, indent=4)



# Function to read data from JSON files
def handle_json(file_path):
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)

        for data in json_data:
            print(f"File name: {file_path} --> Name: {data['name']}, Country: {data['country']}")



def main():
    # List of JSON files to be created and processed
    json_files = ['file1.json', 'file2.json', 'file3.json']

    # Generate JSON files with fake data
    for file in json_files:
        make_jsons(file)


    threads = []
    
    # Create threads for processing different files concurrently
    for file in json_files:
        thread = threading.Thread(target=handle_json, args=(file,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()




if __name__ == "__main__":
    main()