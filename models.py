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
    
    def get_email(self):
        return self._email
    
    def get_created_at(self):
        return self._created_at
    
    def __str__(self):
        return f"{self.get_name()} | {self.get_phone()} | {self.get_email()} | {self.get_created_at()}"
    

class Contact(Person):
    def __init__(self, name, phone, email):
        super().__init__(name,phone)
        self._email = email
        self._created_at = datetime.now().strftime("%Y-%M-%D %H:%M:%S")

