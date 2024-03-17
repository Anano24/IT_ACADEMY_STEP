# შექმენით კლასი Product ატრიბუტებით name, price, quantity, შექმენით კლასის რამდენიმე ობიექტი,
# დაამატეთ ლისტში, დაწერეთ სერიალიზაციის მეთოდი, რომ კლასი გადაითარგმნოს JSON ფორმატში და
# ჩაწერეთ ფაილში, შემდეგ წაიკითხეთ ეს ფაილი, დაწერეთ დესერიალიზაციის მეთოდი, რომ ინფორმაცია
# გადაითარგმნოს Product კლასში და და ბეჭდეთ ყველა პროდუქტის ინფორმაცია

import json


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price}, {self.quantity}'
    

def serialize_product(obj):
    if isinstance(obj, Product):
        return {'name': obj.name, 'price': obj.price, 'quantity': obj.quantity}
    raise TypeError('Expected a Product instance')


def deserialize_product(json_obj):
    if isinstance(json_obj, dict) and 'name' in json_obj and 'price' in json_obj and 'quantity' in json_obj:
        return Product(json_obj['name'], json_obj['price'], json_obj['quantity'])
    raise ValueError('Invalid JSON format for Product')



def main():

    product_1 = Product('product_1', 300, 15)
    product_2 = Product('product_2', 500, 110)
    product_3 = Product('product_3', 1000, 205)
    product_list = [product_1, product_2, product_3]


    # Serialization
    with open('json_file.json', 'w') as json_file:
        json_object = json.dump(product_list, json_file, default=serialize_product, indent=4)


    # Deserialization
    with open('json_file.json', 'r') as json_file:
        deserialized_product = json.load(json_file, object_hook=deserialize_product)
        for product in deserialized_product:
            print(product)




if __name__ == "__main__":
    main()

