from room import Room
from player import Player
from item import Item

item = {
    'sword': Item('sword', 'iron broadsword'),
    'lantern': Item('lantern', 'oil lantnern')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['sword'], item['lantern']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Adam', room['outside'], [])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
selection = ''

print(f'\n*****\n{player.current_room}\n*****')

while True:
    
    selection = input("\nEnter 'n', 's', 'e', or 'w' to move\n'get <item>' to pick up an item\n'drop <item>' to drop an item\n'i' or 'inventory' to view your items\nor 'q' to quit: ")
    
    selection = selection.split(' ')
    
    if len(selection) == 1:
        
        selection = selection[0]
    
        if selection == 'n':
            try:
                player.current_room = player.current_room.n_to
                print('\n...Moving north...')
                print(f'\n*****\n{player.current_room}\n*****')

            except AttributeError:
                print('\nCannot travel north from here')
        
        elif selection == 's':
            try:
                player.current_room = player.current_room.s_to
                print('\n...Moving south...')
                print(f'\n*****\n{player.current_room}\n*****')
        
            except AttributeError:
                print('\nCannot travel south from here')
        
        elif selection == 'e':
            try:
                player.current_room = player.current_room.e_to
                print('\n...Moving east...')
                print(f'\n*****\n{player.current_room}\n*****')

        
            except AttributeError:
                print('\nCannot travel east from here')
        
        elif selection == 'w':
            try:
                player.current_room = player.current_room.w_to
                print('\n...Moving west...')
                print(f'\n*****\n{player.current_room}\n*****')
        
            except AttributeError:
                print('\nCannot travel west from here')
                
        elif selection == 'q':
            print('\nThank you for playing!\n')
            break
        
        elif selection == 'i' or selection == 'inventory':
            if len(player.inventory) == 0:
                print('\nYou are not carrying any items')
            else:
                print('\nYou are carrying the following items:')
                for i in player.inventory:
                    print(f' - {i}\n')
            
        else:
            print('\nPlease enter a valid selection')
    
    else:
        if selection[0] == 'get':
            name = selection[1]
            
            if item[name] in player.current_room.items:
                player.current_room.items.remove(item[name])
                player.inventory.append(item[name])
                item[name].on_take()
                
            else:
                print(f'\nNo {name} here')
        
        elif selection[0] == 'drop':
            name = selection[1]
            
            if item[name] in player.inventory:
                player.inventory.remove(item[name])
                player.current_room.items.append(item[name])
                item[name].on_drop()
            
            else:
                print(f'\nYou do not have a {name}')
        
        else:
            print('\nPlease enter a valid selection')
            
    