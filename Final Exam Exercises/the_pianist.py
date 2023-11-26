def add_function(piece: str, composer: str, key: str, pieces: list):
    if piece not in pieces:
        new_piece = {'piece': piece, 'composer': composer, 'key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")
        return new_piece
    print(f"{piece} is already in the collection!")
    return False

def main_func():
    num = int(input())
    piano_pieces = []

    for _ in range(num):
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

        elif action == 'Remove'
