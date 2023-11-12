name = 'Ivan'
age = 39

# New formatting style
text = 'My name is %s and I am %d years old.' % (name, age)
print(text)

# The old-fashioned one
text = f'My name is {name} and I am {age} years old.'
print(text)

# Third one
price = 20.5
quantity = 10
order = 'The total cost is ${:.2f} for {} items'.format(price * quantity, quantity)
print(order)