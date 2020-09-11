# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    
    def __str__(self):
        ret = f'Location: {self.name}\n\nDescription: {self.description}\n\nItems: '
        
        if len(self.items) > 0:
            for item in self.items:
                ret += '\n - ' + item.name
        else:
            ret += 'none\n'
        
        return ret