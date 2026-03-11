import unittest
from models import Contact, ContactManager
import os
import tempfile

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

    def test_find_by_email(self):
        manager = ContactManager()
        contact = Contact("Lis Pireva", "07718833017", "lis@example.com")
        manager.add_contact(contact)
        result = manager.find_by_email("lis@example.com")
        self.assertIsNotNone(result)
    
    def test_update_contact(self):
        manager = ContactManager()
        contact = Contact("Lis Pireva", "07718833017", "lis@example.com")
        manager.add_contact(contact)
        manager.update_contact("lis@example.com", new_name="Lis Updated")
        result = manager.find_by_email("lis@example.com")
        self.assertEqual(result.get_name(), "Lis Updated")

    def test_save_and_load(self):
        temp = tempfile.NamedTemporaryFile(delete=False)
        temp.close()

        manager = ContactManager(temp.name)
        contact = Contact("Lis Pireva", "07718833017", "lis@example.com")
        manager.add_contact(contact)
        manager.save_contacts()

        new_manager = ContactManager(temp.name)
        new_manager.load_contacts()

        self.assertEqual(len(new_manager.get_all_contacts()), 1)
        os.remove(temp.name)
        
if __name__ == "__main__":
    unittest.main()