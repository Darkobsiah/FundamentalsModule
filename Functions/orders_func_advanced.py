# Define a function
def orders(product: str, quantity: int):
    """

     This function calculates the
     total price of an order and returns it

    :params product, quantity:str, int

    :return: float(total_price)
    """

    return {
        'coffee': quantity * 1.5,
        'water': quantity * 1,
        'coke': quantity * 1.4,
        'snacks': quantity * 2
    }.get(product)

item = input()
quantity = int(input())
result = orders(item, quantity)
print(f"{result:.2f}")
# Read User input