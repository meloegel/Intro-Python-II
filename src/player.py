# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.backpack = []

    def __str__(self):
        return f'Player: {self.name}, {self.location}'

    def take(self, item):
        self.backpack.append(item)

    def drop(self, item):
       del self.backpack[item]
    