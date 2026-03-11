import re

from datetime import datetime


class Person:
    def __init__(self, name, phone):
        self._name = ""
        self._phone = ""
        self.set_name(name)
        self.set_phone(phone)
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        name = name.strip()
        if not name:
            raise ValueError("You must fill out a name")
        self._name = name.title()
    
    def get_phone(self):
        return self._phone
    
    def set_phone(self, phone):
        phone = phone.strip()
        phone_pattern = r"^\+?\d[\d\s-]{8,14}\d$"
        if not re.fullmatch(phone_pattern, phone):
            raise ValueError("You must fill out a valid number")
        self._phone = phone

class Contact(Person):
    def __init__(self, name, phone, email, created_at=None):
        super().__init__(name, phone)

        if created_at is None:
            self._created_at = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
        else:
            self._created_at = created_at

        self._email = ""
        self.set_email(email)
    
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        email = email.strip()
        email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if not re.fullmatch(email_pattern, email):
            raise ValueError("You must fill out a valid email")
        self._email = email.lower()
    
    def get_created_at(self):
        return self._created_at
    
    def __str__(self):
        return f"{self.get_name()} | {self.get_phone()} | {self.get_email()} | {self.get_created_at()}"
    
    def to_line(self):
        return f"{self.get_name()}|{self.get_phone()}|{self.get_email()}|{self.get_created_at()}"
    
    @classmethod
    def from_line(cls, line):
        parts = line.strip().split("|")

        if len(parts) != 4:
            raise ValueError("Contact data is corrupted")
        name, phone, email, created_at = parts
        return cls(name, phone, email, created_at)

class ContactManager:
    def __init__(self, filename="contacts.txt"):
        self.filename = filename
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def get_all_contacts(self):
        return self.contacts
    
    def find_by_name(self, name):
        name = name.strip().lower()
        matches = []
        for contact in self.contacts:
            if name in contact.get_name().lower():
                matches.append(contact)
        return matches
    
    def find_by_email(self, email):
        email = email.strip().lower()
        for contact in self.contacts:
            if contact.get_email() == email:
                return contact
        return None
    
    def update_contact(self, email, new_name=None, new_phone=None, new_email=None):
        contact = self.find_by_email(email)
        if contact is None:
            return False
        if new_name:
            contact.set_name(new_name)
        if new_phone:
            contact.set_phone(new_phone)
        if new_email:
            contact.set_email(new_email)
        return True

    def save_contacts(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for contact in self.contacts:
                file.write(contact.to_line())
    
    def load_contacts(self):
        self.contacts = []

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        self.contacts.append(Contact.from_line(line))

        except FileNotFoundError:
            with open(self.filename, "w", encoding="utf-8"):
                pass