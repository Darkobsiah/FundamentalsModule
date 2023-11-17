# Read User input
tickets = [ticket.strip() for ticket in input().split(', ')]
valid_symbols = ['@', '#', '$']

for ticket in tickets:
    if len(ticket) == 20:
        left_part = ticket[10:]
        right_part = ticket[:10]
        for symbol in valid_symbols:
            for _ in range(10 + 1, 6):
                print(symbol * _)

# Print User output
print(tickets)