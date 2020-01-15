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

# print(type(room))

outside=Room( "Outside Cave Entrance","North of you, the cave mount beckons",['stick', 'rock', 'torch'])
foyer=Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.",['candle stick','broken mirror'])
overlook=Room("Grand Overlook","A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", ['old rope', 'empty bucket'] )
narrow=Room("Narrow Passage","The narrow passage bends here from west to north. The smell of gold permeates the air.", ['only darkness'] )
treasure=Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",['dust','ash','note'] )

# intitial player condition
playerOne = Player(outside.name, ['matches'])

# start of game code

def cls():
    print("\n" * 100)


def OutsideActions():
   
   outside_room_options = ["n", "f"]
   user_choice = " "
   while user_choice not in outside_room_options:
        cls()
        print(F'''you suddenly awake from restles sleep and find yourself at the {outside.name}, {outside.description}...  what do you do?
       n) enter the cave
       f) look around for items...''') 
        user_choice = input("make your choice: ")
        if user_choice == outside_room_options[0]:
            foyerActions()
        elif user_choice == outside_room_options[1]:
            itemsAction()

def foyerActions():
    
    playerOne.location = foyer.name
    foyer_room_options = ['n','s','e','f']
    user_choice = ""
    while user_choice not in foyer_room_options:
        cls()
        print(F'''you slowly enter the{foyer.name}, {foyer.description}... what do you do?
        n) follow the passage toward the overlook
        s) go back outside
        e) follow the narrow passage..is that the smell of gold?
        f) search the foyer for items''')
        user_choice = input("make your choice ")
        if user_choice == foyer_room_options[1]:
            OutsideActions()
        elif user_choice == foyer_room_options[0]:
            OverlookOptions()

def OverlookOptions():

    playerOne.location = overlook.name
OutsideActions()