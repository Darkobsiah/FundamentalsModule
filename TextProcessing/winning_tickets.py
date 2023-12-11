# Define the function to check each ticket
def check_ticket(ticket: str) -> str:
    if len(ticket) != 20:
        return f'invalid ticket'
    matching_symbols = ['@', '#', '$', '^']
    left_side = ticket[:10]
    right_side = ticket[10:]
    for match_symbol in matching_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_combination = uninterrupted_match_length * match_symbol
            if winning_combination in left_side and winning_combination in right_side:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


# Read User input
tickets = [ticket.strip() for ticket in input().split(', ')]
for each in tickets:
    print(check_ticket(each))
