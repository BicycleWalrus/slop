#!/usr/bin/env python3

"""TPatrick | Alta3 Research
   Driving a simple game framework with a Dictionary Object"""

def showInstructions():
    """Show the game instructions when called"""
    # Print a main menu and the commands
    print('''
    RPG Game
    ========
    Get to the Garden with a key and a potion to win! Avoid the monsters! 
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current status
    print('----------------------------')
    print(f'You are in the {currentRoom}')
    # print the current inventory
    print(f'Inventory: {str(inventory)}')
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("----------------------------")

inventory = []

rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'west' : 'Foyer',
                'item' : 'key'
               },
            'Foyer' : {
                'east' : 'Hall',
                'item' : 'sword'
               },
            'Kitchen' : {
                'north' : 'Hall',
                'item' : 'monster'
               },
            'Dining Room' : {
                'west' : 'Hall',
                'south' : 'Garden',
                'item' : 'potion'
               },
            'Garden' : {
                'north' : 'Dining Room'
               }
        }

currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()

    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split(" ", 1)

    # if user types 'go' first
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
    else:
        print('There is no passage that direction.')

    if move[0] == 'get' :
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to the inventory
            inventory += [move[1]]
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        if "sword" in inventory:
            print('There was a monster, but you slayed it with your sword!')
            del rooms[currentRoom]['item']
        else:
            print('A monster has got you... GAME OVER!')
            break

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the Legendary Key of Smogenrog and the Magic Potion of life! YOU WIN!')
        break
