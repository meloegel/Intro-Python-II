# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item =[item]

    def __str__(self):
        return f'Room: {self.name}, Description: {self.description}'

    def remove_item(self, item):
        del self.item[item]

    def add_item(self, item):
        self.item.append(item)