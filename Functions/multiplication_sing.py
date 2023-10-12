# Read User input
number_list = [int(input()), int(input()), int(input())]
number_of_negatives = 0

for num in number_list:
    if num < 0:
        number_of_negatives += 1

if 0 in number_list:
    print('zero')
elif number_of_negatives == 1 or number_of_negatives == 3:
    print('negative')
else:
    print('positive')