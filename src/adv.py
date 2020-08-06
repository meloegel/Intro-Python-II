from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons\n", Item('Torch')),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run all directions\n""", Item('Sword')),

    'dungeon':    Room("Dungeon", """A dimly lit dungeon with torcher devices
in every corner. A long dark hallway appears to the West, it is lit by a flame
at the far end. A dusty passage to the East\n""", Item('Bloody Rag')),

    'guards_quarters':    Room("Guards Quarters", """A well lit room with 
many beds and personal item spread about. The room has been well lived in but
all of the guards are long dead, only skeletons remain at the tables. To the 
North and East you see a door\n""", Item('Iron Helm')),

    'map_room':    Room("Map Room", """A well lit, well decorated map room with 
many books lining the walls. To the South and East there are doors\n""", Item('Map')),

    'great_hall':    Room("Great Hall", """A grand hall stands before you full decorated
and awaiting a feast, the only problem a think layer of dust lies over everything in
sight. There are doors at both ends of the hall (East and West).\n""", Item('Aged Brandy')),

    'secret_passage':    Room("Secret Passage", """Found by accidently leaning
agaisnt the wall a secret door swings open in the Dungeon to the South. Inside 
it is decorated incrediably and houses a secrene meditation pond and cherry 
blossom. You have found the real treasure located within\n""", Item('Inner Peace')),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.\n""", Item('Health Potion')),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.\n""", Item('Axe')),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.\n""", Item('Treasure Chest')),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['dungeon']
room['dungeon'].e_to = room['foyer']
room['dungeon'].w_to = room['guards_quarters']
room['dungeon'].s_to = room['secret_passage']
room['secret_passage'].n_to = room['dungeon']
room['guards_quarters'].e_to = room['dungeon']
room['guards_quarters'].n_to = room['map_room']
room['map_room'].s_to = room['guards_quarters']
room['map_room'].e_to = room['great_hall']
room['great_hall'].w_to = room['map_room']
room['great_hall'].e_to = room['overlook']
room['overlook'].w_to = room['great_hall']
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

print('''
 __       __            __                                                    ________                                       __                     
|  \  _  |  \          |  \                                                  |        \                                     |  \                    
| $$ / \ | $$  ______  | $$  _______   ______   ______ ____    ______         \$$$$$$$$______   ______  __     __   ______  | $$  ______    ______  
| $$/  $\| $$ /      \ | $$ /       \ /      \ |      \    \  /      \          | $$  /      \ |      \|  \   /  \ /      \ | $$ /      \  /      \ 
| $$  $$$\ $$|  $$$$$$\| $$|  $$$$$$$|  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\         | $$ |  $$$$$$\ \$$$$$$\\$$\ /  $$|  $$$$$$\| $$|  $$$$$$\|  $$$$$$|
| $$ $$\$$\$$| $$    $$| $$| $$      | $$  | $$| $$ | $$ | $$| $$    $$         | $$ | $$   \$$/      $$ \$$\  $$ | $$    $$| $$| $$    $$| $$   \$$
| $$$$  \$$$$| $$$$$$$$| $$| $$_____ | $$__/ $$| $$ | $$ | $$| $$$$$$$$         | $$ | $$     |  $$$$$$$  \$$ $$  | $$$$$$$$| $$| $$$$$$$$| $$      
| $$$    \$$$ \$$     \| $$ \$$     \ \$$    $$| $$ | $$ | $$ \$$     \         | $$ | $$      \$$    $$   \$$$    \$$     \| $$ \$$     \| $$      
 \$$      \$$  \$$$$$$$ \$$  \$$$$$$$  \$$$$$$  \$$  \$$  \$$  \$$$$$$$          \$$  \$$       \$$$$$$$    \$      \$$$$$$$ \$$  \$$$$$$$ \$$      
                                                                                                                                                                                                                                                                                          
 ''')
# Write a loop that:
while True:
    print('---------------------------------------------------------------------------')
    current_room = player.location
    player_backpack = [x.name for x in player.backpack] if len(player.backpack) else 'Nothing'
    room_items = [x.name for x in current_room.item] if len(current_room.item) else 'Nothing'
    print(f'Current location: {current_room.name} \n\n. Room description: {current_room.description}\n. Room contents: {room_items}')
    print(f'\nYour backpack contains: {player_backpack} \n')
    print('Enter: \n n for North \n s for South \n e for East \n w for West \n q to quit \n\n For items enter: \n take item_name \n drop item_name \n')
    print('Where would you like to go?')
    command = input('>')

    take_drop_command = command[0:4]
    item = command[5:]

    if command[0] == 'q':
        print(f'Goodbye {player_name}')
        break
    elif command == 'n':
        if hasattr(current_room, 'n_to'):
            print('Moving north')
            player.location = current_room.n_to
        else:
            print('Location does not exist')
    elif command == 's':
        if hasattr(current_room, 's_to'):
            print('Moving south')
            player.location = current_room.s_to
        else:
            print('Location does not exist')
    elif command == 'e':
        if hasattr(current_room, 'e_to'):
            print('Moving east')
            player.location = current_room.e_to
        else:
            print('Location does not exist')
    elif command == 'w':
        if hasattr(current_room, 'w_to'):
            print('Moving west')
            player.location = current_room.w_to
        else:
            print('Location does not exist')
    elif take_drop_command == 'take':
        item_list = [i.name for i in current_room.item]
        print(item_list)
        item_index = item_list.index(item)
        print(item_index)
        player.take(current_room.item[item_index])
        current_room.remove_item(item_index)
    elif take_drop_command == 'drop':
        item_list = [i.name for i in player.backpack]
        item_index = item_list.index(item)
        current_room.add_item(player.backpack[item])
        player.drop(item_index)       
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
