def create_a_car(name: str, distance: int, fuel: int) -> dict:
    """
    This function take 3 params from the main.
    Initialise a dictionary with the car information given
    and returns it to the main
    """
    return {'name': name, 'distance': distance, 'fuel': fuel}


def drive_car(vehicle: str, mileage: int, fuel_needed: int, info):
    for car in info:
        if car['name'] == vehicle:
            if car['fuel'] >= fuel_needed:
                car['fuel'] -= fuel_needed
                car['distance'] += mileage
            else:
                print('Not enough fuel to make that ride')

def main_function():
    """"
    This is the main function. Here we will implement
    the essentials of the logic in this exercises.
    We will also call the other additional functions
    when we need them. Okay, lets go!
    """
    num = int(input())
    car_credentials = []
    for car in range(num):
        car_information = input().split('|')
        car_model, mileage, fuel_available = car_information[0], int(car_information[1]), int(car_information[2])
        current_car = create_a_car(car_model, mileage, fuel_available)
        car_credentials.append(current_car)

    while True:
        command = input()

        if command == 'Stop':
            break

        command = command.split(' : ')
        # Drive : Mercedes CLS : 94 : 11
        if command[0] == 'Drive':
            car, distance, fuel = command[1], int(command[2]), int(command[3])
            drive_car(car, distance, fuel, car_credentials)


main_function()