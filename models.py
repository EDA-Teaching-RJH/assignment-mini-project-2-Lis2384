import re #Imports the regular expressions module for validating numbers and emails

from datetime import datetime #Imports the date and time


class Person: # makes class to store personal details
    def __init__(self, name, phone): #sets up your name and number
        self._name = ""
        self._phone = ""
        self.set_name(name) #validates name
        self.set_phone(phone) # validates number
    
    def get_name(self): #returns a your name
        return self._name
    
    def set_name(self, name): #cleans and validates name 
        name = name.strip()
        if not name:
            raise ValueError("You must fill out a name")
        self._name = name.title()
    
    def get_phone(self): # returns your number
        return self._phone
    
    def set_phone(self, phone): # cleans and validates number
        phone = phone.strip()
        phone_pattern = r"^\+?\d[\d\s-]{8,14}\d$" # validates number
        if not re.fullmatch(phone_pattern, phone): #gives error if number does use correct format
            raise ValueError("You must fill out a valid number")
        self._phone = phone

class Contact(Person):
    def __init__(self, name, phone, email, created_at=None): #sets up details from previous class
        super().__init__(name, phone) #tells class to set name and number

        if created_at is None: # if no date is provided, it will use the current date and time
            self._created_at = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
        else:
            self._created_at = created_at

        self._email = "" #sets defealt empty value for emails
        self.set_email(email) #validates your email address
    
    def get_email(self): # returns your email
        return self._email
    
    def set_email(self, email): #cleans and validates email after its been updated
        email = email.strip()
        email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$" #validates email
        if not re.fullmatch(email_pattern, email): # gives error if email format is wrong
            raise ValueError("You must fill out a valid email")
        self._email = email.lower()
    
    def get_created_at(self): #returns date and time of the contact
        return self._created_at
    
    def __str__(self): # returns contact details as a string
        return f"{self.get_name()} | {self.get_phone()} | {self.get_email()} | {self.get_created_at()}"
    
    def to_line(self): # converts to string
        return f"{self.get_name()}|{self.get_phone()}|{self.get_email()}|{self.get_created_at()}"
    
    @classmethod
    def from_line(cls, line):
        parts = line.strip().split("|") #splits saved line into seperate contact details

        if len(parts) != 4: # checks if data saved with correct number of parts
            raise ValueError("Contact data is corrupted")
        name, phone, email, created_at = parts
        return cls(name, phone, email, created_at) # returns contact with extracted values

class ContactManager: # manages contacts
    def __init__(self, filename="contacts.txt"): #sets file name and makes empty contact list
        self.filename = filename
        self.contacts = []

    def add_contact(self, contact): # adds new contact to contact list
        self.contacts.append(contact)
    
    def get_all_contacts(self): # returns all stored contacts
        return self.contacts
    
    def find_by_name(self, name): # searchs for contact by name given
        name = name.strip().lower()
        matches = [] # stores matching contacts in a list
        for contact in self.contacts: # loops every contact in contact list
            if name in contact.get_name().lower(): 
                matches.append(contact)
        return matches
    
    def find_by_email(self, email): #searches for contact by email given
        email = email.strip().lower()
        for contact in self.contacts: # loops every contact in contact list
            if contact.get_email() == email:
                return contact
        return None
    
    def update_contact(self, email, new_name=None, new_phone=None, new_email=None): #updates contact details using email
        contact = self.find_by_email(email) #finds by email
        if contact is None:
            return False #returns false if doesnt exist
        if new_name: #update name if provided
            contact.set_name(new_name)
        if new_phone: #update phone number if provided
            contact.set_phone(new_phone)
        if new_email: #update email if provided
            contact.set_email(new_email)
        return True

    def save_contacts(self): #saves contacts to file
        with open(self.filename, "w", encoding="utf-8") as file: #open file in write mode to store contact data
            for contact in self.contacts: #writes contact in file
                file.write(contact.to_line())
    
    def load_contacts(self): # loads all contacts from file into program
        self.contacts = [] #clears current contact list before loading saved contacts

        try: #try to open and read contacts file
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file: #read the file line by line
                    line = line.strip()
                    if line: #only processes if the line is not empty
                        self.contacts.append(Contact.from_line(line)) #converts line into a contact and adds it to the list

        except FileNotFoundError: #if the file does not exist make a new empty contacts file
            with open(self.filename, "w", encoding="utf-8"):
                pass