def office_chairs(room_number: int)-> str:
    chairs_left = 0
    for room in range(1, room_number + 1):
        chairs, num = input().split()
        difference = len(chairs) - int(num)
        if difference < 0:
            print(f'{abs(difference)} more chairs needed in room {room}')
        chairs_left += difference
    if chairs_left > 0:
        print(f"Game On, {chairs_left} free chairs left")
    return True


# Read User input
number_of_rooms = int(input())
result = office_chairs(number_of_rooms)
