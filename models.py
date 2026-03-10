import re

from datetime import datetime


class Person:
    def __init__(self, name, phone):
        self._name = name
        self._phone = phone
    
    def get_name(self):
        return self._name
    
    def get_phone(self):
        return self.phone

