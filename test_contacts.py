import unittest
from models import Contact

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

if __name__ == "__main__":
    unittest.main()