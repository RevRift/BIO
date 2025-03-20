import time

class Room:
    def __init__(self, char, has_even_visits, exits, exits_visits):
        self.char = char # unused but it makes sense to store this
        self.has_even_visits = has_even_visits
        self.exits = exits
        self.exit_has_even_visits = exits_visits

def get_all_connections(plan):
    chosen = set()
    ret = dict()

    while plan:
        char = 'A'
        while char in chosen or char in plan:
            char = chr(ord(char) + 1)
        chosen.add(char)
        ret[char] = ret.get(char, '') + plan[0]
        ret[plan[0]] = ret.get(plan[0], '') + char
        plan = plan[1:]
    
    char1, char2 = set(chr(ord('A') + i) for i in range(len(chosen) + 2)) - chosen
    ret[char1] = ret.get(char1, '') + char2
    ret[char2] = ret.get(char2, '') + char1

    for char in ret:
        ret[char] = ''.join(sorted(ret[char]))

    return ret

def find_end_room(num_of_moves):
    rooms = {char: Room(char, True, connections, [True] * len(connections)) for char, connections in all_connections.items()}
    room_char = 'A'

    for move_number in range(num_of_moves):
        room = rooms[room_char]
        room.has_even_visits = not room.has_even_visits
        if not room.has_even_visits:
            room_char = room.exits[0]
            room.exit_has_even_visits[0] = not room.exit_has_even_visits[0]
        else:
            for i in range(len(room.exits)):
                if not room.exit_has_even_visits[i]:
                    break
            i = min(i + 1, len(room.exits) - 1)
            room_char = room.exits[i]
            room.exit_has_even_visits[i] = not room.exit_has_even_visits[i]
    return room_char

secret_plan, p, q = input().split()

start_time = time.time()

all_connections = get_all_connections(secret_plan)
for room in sorted(all_connections):
    print(all_connections[room])

print(f'Split: {time.time() - start_time}')

end_room1, end_room2 = find_end_room(int(p)), find_end_room(int(q))
print(end_room1 + end_room2)

print(f'Elapsed: {time.time() - start_time}')

# question 2d
"""
using a generator like this https://github.com/matthewelse/british-informatics-olympiad/blob/master/2020/q2_d.py
solution is a good idea because it tells you the order that pairs are found, allowing you all parts of question 2 with the same function
"""