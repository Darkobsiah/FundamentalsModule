def check_ticket(ticket):
    if len(ticket) != 20:
        return 'invalid ticket'
    winning_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted
