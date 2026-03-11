from models import Contact, ContactManager

manager = ContactManager()

while True:
    print("---Menu---")
    print("1) Add Contact")
    print("2) View Contacts")
    print("3) Search Contacts")
    print("4) Exit)")
    choice = input("Option: ")

    if choice == "1":
        

contact1 = Contact("Lis Pireva", "1234567890", "lis@example.com")
contact2 = Contact("dave", "1234567899", "dave@example.com")

manager.add_contact(contact1)
manager.add_contact(contact2)

for contact in manager.get_all_contacts():
    print(contact)