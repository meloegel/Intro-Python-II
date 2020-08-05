from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
player_name = input('Enter your name:')
player_room = room['outside']
player = Player(player_name, player_room)
print(player)

# Write a loop that:
while True:

    current_room = player.location
    print(f'Current location: {current_room.name}. Room description: {current_room.description}')
    print('Where would you like to go? (Enter n, s, e, w or q to quit')
    command = input('>').split(',')

    if command[0] == 'q':
        print(f'Goodbye {player_name}')
        break
    elif command[0] == 'n':
        if hasattr(current_room, 'n_to'):
            print('Moving north')
            player.location = current_room.n_to
        else:
            print('Location does not exist')
    elif command[0] == 's':
        if hasattr(current_room, 's_to'):
            print('Moving south')
            player.location = current_room.s_to
        else:
            print('Location does not exist')
    elif command[0] == 'e':
        if hasattr(current_room, 'e_to'):
            print('Moving east')
            player.location = current_room.e_to
        else:
            print('Location does not exist')
    elif command[0] == 'w':
        if hasattr(current_room, 'w_to'):
            print('Moving west')
            player.location = current_room.w_to
        else:
            print('Location does not exist')        
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
