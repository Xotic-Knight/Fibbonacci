#dictionary of rooms
rooms = {'road': {'name': 'the road', 'north': 'lawn', 'contents': [],
                   'text': 'The night is dark and lonely and there is no one on the road'},
         'lawn': {'name': 'the lawn', 'east': 'garage', 'south': 'road',
                    'text': 'This seems to be the place for chilling!!!',
                    'contents': ['bench', 'football', 'grass', 'statue']},
         'garage': {'name': 'the garage','north': 'bedroom','east': 'toilet' , 'west': 'lawn',
                     'contents': ['chains', 'car' ,'grass', 'cycle'],
                     'text': 'There is a rack and an iron maiden against the wall\naand some dark stains on the floor.'},
         'bedroom': {'name': 'a bedroom', 'north': 'dining','south': 'garage','east': 'bathroom' ,'west': 'drawing', 'contents': ['sheets', 'bed','lamp'],
                     'text': 'This is clearly a bedroom, but no one has slept\nhere in a long time. Need Company!!!!'},
         'toilet': {'name':'a toilet','north':'bathroom','east':'garage','contents':['toilet paper','handwash'],
                    'text':'Noone has used this room for a while'},
         'drawing': {'name':'the drawing room','south':'lawn','east':'bedroom','contents':['statue','toffee','pen'],
                     'text':'Guests are Not Welcomed'},
         'bathroom':{'name':'the bathroom','north':'kitchen','south':'toilet','west':'bedroom','contents':['soap','shampoo'],
                     'text':'Use it wisely'},
         'dining':{'name':'dining room','south':'bedroom','east':'kitchen','contents':['spoon','fork'],
                   'text':'Eat Here!!!!'},
         'kitchen':{'name':'kitchen','south':'bathroom','west':'dining','contents':['stove','knife','glass'],
                    'text':'Food Prepared Here!!!!'}}
directions = ['north', 'south', 'east', 'west']
current_room = rooms['road']
carrying = []

# game loop
while True:
    # display current location
    print()
    print('You are in {}.'.format(current_room['name']))
    print(current_room['text'])
    # display movable objects
    if current_room['contents']:
        print('In the room are: {}'.format(', '.join(current_room['contents'])))
    # get user input
    command = input('\nWhat do you do? ').strip()
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # bad movement
            print("You can't go that way.")
    # quit game
    elif command.lower() in ('q', 'quit'):
        break
    # gather objects
    elif command.lower().split()[0] == 'get':
        item = command.lower().split()[1]
        if item in current_room['contents']:
            current_room['contents'].remove(item)
            carrying.append(item)
        else:
            print("I don't see that here.")
    # get rid of objects
    elif command.lower().split()[0] == 'drop':
        item = command.lower().split()[1]
        if item in carrying:
            current_room['contents'].append(item)
            carrying.remove(item)
        else:
            print("You aren't carrying that.")
    # bad command
    else:
        print("I don't understand that command.")
