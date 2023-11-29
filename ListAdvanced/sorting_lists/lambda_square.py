def square(x: int) -> int:
    return x*x


numbers = [1, 2, 3, 4, 5]

square_numbers = list(map(square, numbers))

print(square_numbers)
