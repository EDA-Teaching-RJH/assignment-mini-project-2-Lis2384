from models import Contact, ContactManager #Imports the contact and contactmanager from models

manager = ContactManager("contacts.txt") #connecting contact manager to contacts.txt
manager.load_contacts() # Loads all saved contacts from the file

while True: #keeps showing menu untill you exit
    print("---Menu---")
    print("1) Add Contact")
    print("2) View Contacts")
    print("3) Search Contacts")
    print("4) Update Contact")
    print("5) Exit")
    choice = input("Option: ")

    if choice == "1": # Selects the first choice of adding a contact
        name = input("Name: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        try: #tries to create and save contact, also catches invalid inputs
            contact = Contact(name, phone, email)
            manager.add_contact(contact)
            manager.save_contacts()
            print("Contact Added")
        except ValueError as error:
            print(error)
        
    
    elif choice == "2": # Selects the second choice of showing all contacts saved
        for contact in manager.get_all_contacts():
            print(contact)
    
    elif choice == "3": # Selects the third option of searching a contact by email input
        email = input("Email you want to search: ")
        contact = manager.find_by_email(email)
        if contact: # Checks whether email is in system
            print(contact)
        else:
            print("Contact not found")
    
    elif choice == "4": # Selects the fourth choice of updating an existing contact
        email = input("current email: ")
        new_name = input("New name: ").strip()
        new_phone = input("New phone number: ").strip()
        new_email = input("New email: ").strip()

        try: # Tries to update contact details and check for invalid input
            updated = manager.update_contact(
                email,
                new_name if new_name else None,
                new_phone if new_phone else None,
                new_email if new_email else None
            )
            manager.save_contacts() # Saves the contacts changed
            if updated:
                print("Contact updated")
            else:
                print("Not found")
        except ValueError as error:
            print(error)
    
    elif choice == "5": # Selects option 5 which saves all contacts and ends the program
        manager.save_contacts()
        print("Goodbye")
        break

for contact in manager.get_all_contacts():
    print(contact) # Prints all contacts after the program ends (mostly just a safety check)