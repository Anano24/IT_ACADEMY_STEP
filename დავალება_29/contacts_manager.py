class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        if name in self.contacts:
            return f"Contact '{name}' already exists."
        else:
            self.contacts[name] = phone_number
            return f"Contact '{name}' added successfully."

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return f"Contact '{name}' removed successfully."
        else:
            return f"Contact '{name}' not found."

    def search_contact(self, name):
        if name in self.contacts:
            return f"Name: {name}, Phone Number: {self.contacts[name]}"
        else:
            return f"Contact '{name}' not found."

    def display_contacts(self):
        result = "Contacts:\n"
        if self.contacts:
            for name, phone_number in self.contacts.items():
                result += f"Name: {name}, Phone Number: {phone_number}\n"
            return result
        else:
            return "No contacts found."
        
