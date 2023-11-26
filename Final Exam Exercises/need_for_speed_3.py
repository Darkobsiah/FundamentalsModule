def create_a_car(name: str, distance: int, fuel: int) -> dict:
    """
    This function take 3 params from the main.
    Initialise a dictionary with the car information given
    and returns it to the main
    """
    return {'name': name, 'distance': distance, 'fuel': fuel}


def drive_car(vehicle: str, mileage: int, fuel_needed: int, credentials: list):
    for car in credentials:
        if car['name'] == vehicle:
            if car['fuel'] >= fuel_needed:
                car['fuel'] -= fuel_needed
                car['distance'] += mileage
                print(f"{car['name']} driven for {mileage} kilometres. {fuel_needed} liters of fuel consumed.")
            else:
                print('Not enough fuel to make that ride')
            if car['distance'] >= 100000:
                credentials.remove(car)
    return credentials


def refuel_tank(model, fuel_to_add, credentials: list):
    for car in credentials:
        if car['name'] == model:
            print(car)


def main_function():
    """"
    This is the main function. Here we will implement
    the essentials of the logic in this exercises.
    We will also call the other additional functions
    when we need them. Okay, lets go!
    """
    car_credentials = []
    num = int(input())
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
            car_credentials = drive_car(car, distance, fuel, car_credentials)

        elif command[0] == 'Refuel':
            # "Refuel : {car} : {fuel}":
            car, fuel = command[1], command[2]
            refuel_tank(car, fuel, car_credentials)


main_function()
