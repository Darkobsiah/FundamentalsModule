def create_a_car(name: str, distance: int, fuel: int) -> dict:
    """
    This function take 3 params from the main.
    Initialise a dictionary with the car information given
    and returns it to the main
    """
    return {'name': name, 'distance': distance, 'fuel': fuel}


def main_function():
    """"
    This is the main function. Here we will implement
    the essentials of the logic in this exercises.
    We will also call the other additional functions
    when we need them. Okay, lets go!
    """
    num = int(input())
    for car in range(num):
        car_information = input().split('|')
        car_model, mileage, fuel_available = car_information[1], int(car_information[2]), int(car_information[3])
        create_a_car(car_model, mileage, fuel_available)