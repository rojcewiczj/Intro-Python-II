# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location, items=[]):
        self.name= 'john'
        self.location = location
        self.items = items
    def add_item(self, item):
        self.items.append(item)
    

    
