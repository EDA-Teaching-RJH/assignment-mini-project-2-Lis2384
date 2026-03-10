import unittest
from models import Contact

class TestContact(unittest.TestCase):
    def test_contact_creation(self):
        contact = Contact("Lis Pireva", "1234567890", "lis@example.com")
        self.assertEqual(contact.get_email(), "lis@example.com")

if __name__ == "__main__":
    unittest.main()