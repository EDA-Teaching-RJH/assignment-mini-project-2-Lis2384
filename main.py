from models import Contact

try:
    contact1 = Contact("Lis Pireva", "1234567890", "lis@example.com")
    print(contact1)
except ValueError as error:
    print(error)