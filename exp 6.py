
rooms = {'A': 1, 'B': 1}
position = 'A'

while 0 in rooms.values():
    print("Position:", position)
    
    if rooms[position] == 0:
        print("Cleaning room", position)
        rooms[position] = 1
    else:
        print("Room is clean")
    
    position = 'B' if position == 'A' else 'A'

print("Both rooms are clean!")
