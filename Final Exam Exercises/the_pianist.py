def add_function(piece: str, composer: str, key: str, pieces: list):
    is_there = False
    for okayde in pieces:
        for name, value in okayde.items:
            print(key, value)

    if not is_there:
        new_piece = {'piece': piece, 'composer': composer, 'key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")
        return new_piece
    print(f"{piece} is already in the collection!")
    return False


def remove_piece(piece: str, pieces: list):
    if piece in pieces:
        pieces.remove(piece)


def main_func():
    num = int(input())
    piano_pieces = []

    # Read User info
    for _ in range(num):
        part = input().split('|')
        part, artist, key = part[0], part[1], part[2]
        piano_pieces.append({'part': part, "artist": artist, "key": key})

    while True:
        command = input()
        if command == "Stop":
            break
        command = command.split("|")
        action = command[0]

        if action == "Add":
            part, artist, key = command[1], command[2], command[3]
            element = add_function(part, artist, key, piano_pieces)
            if element:
                piano_pieces.append(element)

        elif action == 'Remove':
            part = command[1]
            remove_piece(part)


if __name__ == '__main__':
    main_func()
