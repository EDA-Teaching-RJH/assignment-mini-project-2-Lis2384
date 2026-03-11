from models import Contact, ContactManager

manager = ContactManager()

while True:
    print("---Menu---")
    print("1) Add Contact")
    print("2) View Contacts")
    print("3) Search Contacts")
    print("4) Update Contact")
    print("5) Exit")
    choice = input("Option: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        try:
            contact = Contact(name, phone, email)
            manager.add_contact(contact)
            print("Contact Added")
        except ValueError as error:
            print(error)
    
    elif choice == "2":
        for contact in manager.get_all_contacts():
            print(contact)
    
    elif choice == "3":
        email = input("Email you want to search: ")
        contact = manager.find_by_email(email)
        if contact:
            print(contact)
        else:
            print("Contact not found")
    
    elif choice == "5":
        break

for contact in manager.get_all_contacts():
    print(contact)