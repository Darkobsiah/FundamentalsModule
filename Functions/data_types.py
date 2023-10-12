# Define the function
def data_types(type: str, object: str):
    if type == 'int':
        return int(object) * 2
    elif type == 'real':
        result = int(object) *  1.5
        return f'{result:.2f}'
    elif type == 'string':
        return f'${object}$'


# Read User input
type_of_string = input()
the_string = input()

# Print
print(data_types(type_of_string, the_string))