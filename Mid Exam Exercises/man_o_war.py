# Define a function for the fire command
def fire_func(warship: list, index: int, damage: int):
    if 0 <= index < len(warship):
        warship[index] -= damage
        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")


# Define a function for the defend command
def defend_func(pirate_ship: list, start_index: int, end_index: int, damage):
    if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
        for i in range(start_index, end_index + 1):
            pirate_ship[i] -= damage

            if pirate_ship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()


def repair_func(pirate_ship: list, index: int, health: int):
    if 0 <= index < len(pirate_ship):
        # check if the index value is over max health and deny it
        pirate_ship[index] = min(pirate_ship[index] + health, maximum_health)

def status_func(pirate_ship: list, max_health: int):
    counter = 0
    for cell in pirate_ship:
        if cell < max_health * 0.2:
            counter += 1
    print(f"{counter} sections need repair.")


# Read User input
pirate_ship_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
maximum_health = int(input())

while True:
    command = input().split()

    if command[0] == 'Retire':
        break

    type_of_command = command[0]
    if type_of_command == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        fire_func(warship_status, index, damage)


    elif type_of_command == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        defend_func(pirate_ship_status, start_index, end_index, damage)

    elif type_of_command == 'Repair':
        index = int(command[1])
        health = int(command[2])
        repair_func(pirate_ship_status, index,health)


    elif type_of_command == 'Status':
        status_func(pirate_ship_status, maximum_health)


print(f"Pirate ship status: {sum(pirate_ship_status)}")

print(f"Warship status: {sum(warship_status)}")

