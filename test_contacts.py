import unittest #imports unittest module to create and run test cases
from models import Contact, ContactManager #imports contact and contactmanager classes
import os #imports os so the temp test file can be deleted after the test
import tempfile # imports tempfile for save and load testing

class TestContact(unittest.TestCase): # makes test class for checking contact and contactmanager
    def test_contact_creation(self): #test if contact is made correctly
        contact = Contact("Lis Pireva", "+447718833017", "lis@example.com")
        self.assertEqual(contact.get_email(), "lis@example.com")

    def test_invalid_email(self): #test if a invalid email raises an error
        with self.assertRaises(ValueError):
            Contact("Lis Pireva", "+447718833017", "fsdfkjsvb")

    def test_invalid_phone(self): # test if a invalid phone raises error
        with self.assertRaises(ValueError):
                Contact("Lis pireva", "435", "lis@example.com")
    
    def test_add_contact(self): # test if contact can be added to manager
        manager = ContactManager()
        contact = Contact("Lis Pireva", "+447718833017", "lis@example.com")
        manager.add_contact(contact)
        self.assertEqual(len(manager.get_all_contacts()), 1)

    def test_find_by_email(self): #test if contact can be found by email
        manager = ContactManager()
        contact = Contact("Lis Pireva", "07718833017", "lis@example.com")
        manager.add_contact(contact)
        result = manager.find_by_email("lis@example.com")
        self.assertIsNotNone(result)
    
    def test_update_contact(self): #test if contact can be updated
        manager = ContactManager()
        contact = Contact("Lis Pireva", "07718833017", "lis@example.com")
        manager.add_contact(contact)
        manager.update_contact("lis@example.com", new_name="Lis Updated")
        result = manager.find_by_email("lis@example.com")
        self.assertEqual(result.get_name(), "Lis Updated")

    def test_save_and_load(self): #test if contact can be saved to and loaded from
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
        
if __name__ == "__main__":  #run the unit tests when file is executed
    unittest.main()