import unittest
from models import Contact, ContactManager

class TestContact(unittest.TestCase):
    def test_contact_creation(self):
        contact = Contact("Lis Pireva", "+447718833017", "lis@example.com")
        self.assertEqual(contact.get_email(), "lis@example.com")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            Contact("Lis Pireva", "+447718833017", "fsdfkjsvb")

    def test_invalid_phone(self):
        with self.assertRaises(ValueError):
                Contact("Lis pireva", "435", "lis@example.com")
    
    def test_add_contact(self):
        manager = ContactManager()
        contact = Contact("Lis Pireva", "+447718833017", "lis@example.com")
        manager.add_contact(contact)
        self.assertEqual(len(manager.get_all_contacts()), 1)

if __name__ == "__main__":
    unittest.main()