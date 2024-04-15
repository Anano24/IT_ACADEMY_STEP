import unittest
from contacts_manager import ContactManager



class TestContactManager(unittest.TestCase):

    def setUp(self):
        self.manager = ContactManager()

    def test_add_contact(self):
        self.assertEqual(self.manager.add_contact("Nino", "(+995)32521023"), "Contact 'Nino' added successfully.")
        self.assertEqual(self.manager.add_contact("Nika", "55521023"), "Contact 'Nika' added successfully.")
        self.assertEqual(self.manager.add_contact("Nika", "55521023"), "Contact 'Nika' already exists.")
        self.assertEqual(self.manager.add_contact("Nino", "(+995)32521023"), "Contact 'Nino' already exists.")


    def test_remove_contact(self):
        self.assertEqual(self.manager.remove_contact("Nino"), "Contact 'Nino' not found.")

        # Add contacts
        self.manager.add_contact("Mari", "558243288")
        self.manager.add_contact("Gio", "1233300033")

        self.assertEqual(self.manager.remove_contact("Mari"), "Contact 'Mari' removed successfully.")
        self.assertEqual(self.manager.remove_contact("Gio"), "Contact 'Gio' removed successfully.")


    def test_search_contact(self):
        self.assertEqual(self.manager.search_contact("John"), "Contact 'John' not found.")
        
        # Add contacts
        self.manager.add_contact("Nana", "77727888392")
        self.manager.add_contact("Gio", "1233300033")

        self.assertEqual(self.manager.search_contact("Nana"), "Name: Nana, Phone Number: 77727888392")
        self.assertEqual(self.manager.search_contact("Gio"), "Name: Gio, Phone Number: 1233300033")


    def test_display_contacts(self):
        self.assertEqual(self.manager.display_contacts(), "No contacts found.")

        # Add contacts
        self.manager.add_contact("Nana", "77727888392")
        self.manager.add_contact("Gio", "1233300033")

        # Define expected output
        output = "Contacts:\n"
        output += "Name: Nana, Phone Number: 77727888392\n"
        output += "Name: Gio, Phone Number: 1233300033\n"

        # Check if the actual output matches the expected output
        self.assertEqual(self.manager.display_contacts(), output)



if __name__ == "__main__":
    unittest.main()
        